from flask import Flask, render_template, request, jsonify, flash, redirect, url_for
import pymysql
from pymysql.cursors import DictCursor
from urllib.parse import urlparse
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)
app.secret_key = '530 project'

# Database connection details
db_config = {
    'host': '127.0.0.1',
    'database': '530pro',
    'user': '530p',
    'password': '530p'
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check_url', methods=['POST'])
def check_url():
    url_to_check = request.form['url']
    
    conn = pymysql.connect(**db_config, cursorclass=DictCursor)
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT `result` FROM `index` WHERE `url` = %s", (url_to_check,))
            row = cursor.fetchone()
            is_phishing = None

            if row is not None:
                is_phishing = (row['result'] == 1)
    finally:
        conn.close()
    
    if is_phishing is None:
        return render_template('result.html', url=url_to_check, is_phishing=is_phishing, show_analyze_button=True)
    else:
        return render_template('result.html', url=url_to_check, is_phishing=is_phishing, show_analyze_button=False)
        
@app.route('/report_url', methods=['POST'])
def report_url():
    url_to_report = request.form['url']
    report_type = request.form['report_type']
    r = ''
    if report_type == 'safe':
        r = 0
    elif report_type == 'unsafe':
        r = 1
    conn = pymysql.connect(**db_config)
    try:
        with conn.cursor() as cursor:
            cursor.execute(f"INSERT INTO `index` (`url`, `result`) VALUES (%s, %s)", (url_to_report,r))
            conn.commit()
            flash('URL reported successfully! Thank you for your contribution.')
    finally:
        conn.close()
    return redirect(url_for('index'))

@app.route('/unknown', methods=['POST'])
def unknown():
    a_url = request.form['url']
    dc = 0
    is_safe = False

    if '://' not in a_url:
        domain = a_url
    else:
        domain = urlparse(a_url).netloc or urlparse(a_url).path

    urlvoid_url = f"https://www.urlvoid.com/scan/{domain}/"

    response = requests.get(urlvoid_url)

    if response.status_code == 200:

        soup = BeautifulSoup(response.content, 'html.parser')   
        detection_count_span1 = soup.find('span', class_='label label-danger')
        detection_count_span2 = soup.find('span', class_='label label-success')
        
        if detection_count_span1:
            detection_count = detection_count_span1.text
            detections = int(detection_count.split('/')[0])
            if detections >= 1:
                conn = pymysql.connect(**db_config)
                try:
                    with conn.cursor() as cursor:
                        cursor.execute(f"INSERT INTO `index` (`url`, `result`) VALUES ({a_url}, 1)")
                        cursor.execute(f"INSERT INTO `index` (`url`, `result`) VALUES ({domain}, 1)")
                        conn.commit()
                except pymysql.MySQLError as e:
                    print(f"An error occurred while inserting the ananlyzed url into the database: {e}")
                finally:
                    conn.close()
                dc = 1
                is_safe = False
                return render_template('unknown.html', url=domain, is_safe=is_safe, detection_count=dc)

        if detection_count_span2:
            detection_count = detection_count_span2.text
            detections = int(detection_count.split('/')[0])
            if detections == 0:
                conn = pymysql.connect(**db_config)
                try:
                    with conn.cursor() as cursor:
                        cursor.execute(f"INSERT INTO `index` (`url`, `result`) VALUES ({a_url}, 1)")
                        cursor.execute(f"INSERT INTO `index` (`url`, `result`) VALUES ({domain}, 1)")
                        conn.commit()
                except pymysql.MySQLError as e:
                    print(f"An error occurred while inserting the ananlyzed url into the database: {e}")
                finally:
                    conn.close()
                dc = 0
                is_safe = True
                return render_template('unknown.html', url=domain, is_safe=is_safe, detection_count=dc)
        else:
            c_msg = f'Failed to fetch data for {domain}. Try again  Status code: {response.status_code}'
            return render_template('unknown.html', url=domain, msg=c_msg, is_safe=None, detection_count=0)
        
    else:
        d_msg = f'Failed to fetch data for {domain}. Status code: {response.status_code}'
        return render_template('unknown.html', url=domain, msg=d_msg, is_safe=None, detection_count=None)

@app.route('/api_instructions')
def api_instructions():
    return render_template('api.html')

@app.route('/stats')
def stats():
    conn = pymysql.connect(**db_config, cursorclass=DictCursor)
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT COUNT(*) AS total_checked FROM `index`")
            total_checked = cursor.fetchone()['total_checked']

            cursor.execute("SELECT COUNT(*) AS total_unsafe FROM `index` WHERE `result` = 1")
            total_unsafe = cursor.fetchone()['total_unsafe']

            cursor.execute("SELECT COUNT(*) AS total_safe FROM `index` WHERE `result` = 0")
            total_safe = cursor.fetchone()['total_safe']

            cursor.execute("SELECT `url`, COUNT(*) as `count` FROM `index` WHERE `result` = 1 GROUP BY `url` ORDER BY `count` DESC LIMIT 50")
            top_phishing = cursor.fetchall()
    finally:
        conn.close()

    return render_template('stats.html', total_checked=total_checked, total_unsafe=total_unsafe , total_safe=total_safe, top_phishing=top_phishing)


@app.route('/api/check', methods=['POST'])
def api_check_url():
    data = request.json
    url_to_check = data['url']
    
    # Connect to the database
    conn = pymysql.connect(**db_config, cursorclass=DictCursor)
    try:
        with conn.cursor() as cursor:
            # SQL query to check if the URL is in the database
            cursor.execute("SELECT `result` FROM `index` WHERE `url` = %s", (url_to_check,))
            result = cursor.fetchone()
            # If result is not None, the URL was found in the phishing list
            is_phishing = result is not None if result else False
    except pymysql.MySQLError as e:
        print(f"Database error: {e}")
        return jsonify({'error': 'Database error occurred'}), 500
    finally:
        conn.close()

    return jsonify({'url': url_to_check, 'is_phishing': is_phishing})

@app.route('/api/report', methods=['POST'])
def api_report_url():
    data = request.json
    url_to_report = data['url']
    
    conn = pymysql.connect(**db_config)
    try:
        with conn.cursor() as cursor:
            # SQL query to insert the reported URL into the database
            cursor.execute("INSERT INTO `index` (`url`, `website`, `result`) VALUES (%s, 'user_report', 1)", (url_to_report,))
            conn.commit()
    except pymysql.MySQLError as e:
        print(f"Database error: {e}")
        return jsonify({'error': 'Database error occurred'}), 500
    finally:
        conn.close()

    return jsonify({'message': 'URL reported successfully!'})

if __name__ == '__main__':
    app.run(debug=True)
