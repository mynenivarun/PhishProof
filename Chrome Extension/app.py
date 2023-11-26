from flask import Flask, request, jsonify
import pymysql

app = Flask(__name__)

# Establish database connection
conn = pymysql.connect(host='127.0.0.1', database='530pro', user='530p', password='530p')
tbl = 'index'

def is_phishing_link(url):
    link = url
    try:
        with conn.cursor() as cursor:
            # SQL query to search for the URL
            query = f"SELECT * FROM `{tbl}` WHERE `url` = {link}"
            cursor.execute(query, (url,))
            result = cursor.fetchone()
            return result is not None  # Return True if URL is found in the database
    except Exception as e:
        print(f"Error occurred: {e}")
        return False  # Return False in case of an error
    finally:
        conn.commit()

@app.route('/check_url', methods=['POST'])
def check_url():
    urls = request.json['urls']
    results = {url: is_phishing_link(url) for url in urls}
    return jsonify(results)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=1234)
