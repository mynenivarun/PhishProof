# PhishProof
Python-based Web app for verifying Phishing or Fraud Links


## Introduction

Phishing Link Detector is a Flask-based web application that identifies and flags potentially harmful URLs. Leveraging the URLVoid API for URL analysis, this application allows users to check the safety status of URLs, enhancing online safety and awareness.

## Installation & Setup

### Prerequisites

Ensure you have Python 3.6 or later installed on your machine. You can download Python from [python.org](https://www.python.org/downloads/).

### Clone the Repository

To get started, clone the repository to your local machine:

```
git clone https://github.com/your-username/phishing-link-detector.git
cd phishing-link-detector
```

### Install Required Libraries

Install the required Python libraries using pip:

```
pip install requests
pip install urllib3
pip install pymysql
pip install Flask
pip install BeautifulSoup4
```

This command installs Flask for web application development, pymysql for MySQL database interaction, BeautifulSoup4 for HTML parsing, and requests for making HTTP requests.

### Database Configuration

Set up your MySQL database and update the `db_config` in `app.py` with your database credentials:

```
db_config = {
    'host': 'your_database_host',
    'database': 'your_database_name',
    'user': 'your_database_user',
    'password': 'your_database_password'
}
```

### Running the Application

To run the application, execute:

```
python web app.py
```

The application will be accessible at `http://localhost:5000`.

## API Usage

The Phishing Link Detector includes an API that allows users to check URLs programmatically.

### Check URL

**Endpoint:** `/api/check_url`

**Method:** `POST`

**Body:**

```
{
    "url": "http://example.com"
}
```

**Response:**

```
{
    "url": "http://example.com",
    "is_safe": true
}
```

### Reporting URLs

**Endpoint:** `/api/report_url`

**Method:** `POST`

**Body:**

```
{
    "url": "http://example.com",
    "report_type": "unsafe"  // or "safe"
}
```

**Response:**

```
{
    "message": "URL report submitted successfully."
}
```

### Example Usage

You can use tools like `curl` or Postman to interact with the API. Here's an example using `curl`:

```
curl -X POST -H "Content-Type: application/json" -d '{"url": "http://example.com"}' http://localhost:5000/api/check_url
```

## UI Samples (or) ScreenShots

### Basic (Home, API, Stats)
![alt text](https://github.com/mynenivarun/PhishProof/blob/main/ScreenShots/Basic_Home.png "Home Page")
![alt text](https://github.com/mynenivarun/PhishProof/blob/main/ScreenShots/Basic_Api.png "API Page")
![alt text](https://github.com/mynenivarun/PhishProof/blob/main/ScreenShots/Basic_Stats.png "Stats Page")

### API Usage
![alt text](https://github.com/mynenivarun/PhishProof/blob/main/ScreenShots/API_Usage.png "API Usage")

### Reporting Urls Safe/Unsafe
![alt text](https://github.com/mynenivarun/PhishProof/blob/main/ScreenShots/Safe_Report.png "Report Safe")
![alt text](https://github.com/mynenivarun/PhishProof/blob/main/ScreenShots/Safe_Results.png "Results Safe")
![alt text](https://github.com/mynenivarun/PhishProof/blob/main/ScreenShots/Unsafe_Report.png "Report Unsafe")
![alt text](https://github.com/mynenivarun/PhishProof/blob/main/ScreenShots/Unsafe_Results.png "Results Unsafe")

### Stats Before & After Reporting Urls
![alt text](https://github.com/mynenivarun/PhishProof/blob/main/ScreenShots/Screenshot%202023-11-24%20051644.png "Before")
![alt text](https://github.com/mynenivarun/PhishProof/blob/main/ScreenShots/Stats_After.png "After")

### Checking Both Safe/Unsafe if URLs are in the Database
![alt text](https://github.com/mynenivarun/PhishProof/blob/main/ScreenShots/Check_Url1.png "Checking Unsafe")
![alt text](https://github.com/mynenivarun/PhishProof/blob/main/ScreenShots/Check_Url1E.png "Result Unsafe")
![alt text](https://github.com/mynenivarun/PhishProof/blob/main/ScreenShots/Check_Url2.png "Checking Safe")
![alt text](https://github.com/mynenivarun/PhishProof/blob/main/ScreenShots/Check_Url2S.png "Result Safe")

### Checking and Analyzing Both Safe/Unsafe if URLs are not there in the Database
#### 1
![alt text](https://github.com/mynenivarun/PhishProof/blob/main/ScreenShots/1Check_Unkwn_Url.png "Checking Unknown")
![alt text](https://github.com/mynenivarun/PhishProof/blob/main/ScreenShots/1Check_Unkwn_Url_Result.png "Results Unknown")
![alt text](https://github.com/mynenivarun/PhishProof/blob/main/ScreenShots/1Check_Unkwn_Url_Rslt_Ana.png "Analysis Unknown")
#### 2
![alt text](https://github.com/mynenivarun/PhishProof/blob/main/ScreenShots/Check_Unkwn_Url.png "Checking Unknown")
![alt text](https://github.com/mynenivarun/PhishProof/blob/main/ScreenShots/Check_Unkwn_Url_Result.png "Results Unknown")
![alt text](https://github.com/mynenivarun/PhishProof/blob/main/ScreenShots/Check_Unkwn_Url_Rslt_Ana.png "Analysis Unknown")

## Contributions

Contributions to the Phishing Link Detector are welcome. Please fork the repository, make your changes, and submit a pull request.
