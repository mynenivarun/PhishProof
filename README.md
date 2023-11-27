# PhishProof
Python-based Web app for verifying Phishing or Fraud Links


## Introduction

Phishing Link Detector is a Flask-based web application that identifies and flags potentially harmful URLs. Leveraging the URLVoid API for URL analysis, this application allows users to check the safety status of URLs, enhancing online safety and awareness.

## Installation & Setup

### Prerequisites

Ensure you have Python 3.6 or later installed on your machine. You can download Python from [python.org](https://www.python.org/downloads/).

### Clone the Repository

To get started, clone the repository to your local machine:

\```bash
git clone https://github.com/your-username/phishing-link-detector.git
cd phishing-link-detector
\```

### Install Required Libraries

Install the required Python libraries using pip:

\```bash
pip install Flask pymysql BeautifulSoup4 requests
\```

This command installs Flask for web application development, pymysql for MySQL database interaction, BeautifulSoup4 for HTML parsing, and requests for making HTTP requests.

### Database Configuration

Set up your MySQL database and update the `db_config` in `app.py` with your database credentials:

\```python
db_config = {
    'host': 'your_database_host',
    'database': 'your_database_name',
    'user': 'your_database_user',
    'password': 'your_database_password'
}
\```

### Running the Application

To run the application, execute:

\```bash
python app.py
\```

The application will be accessible at `http://localhost:5000`.

## API Usage

The Phishing Link Detector includes an API that allows users to check URLs programmatically.

### Check URL

**Endpoint:** `/api/check_url`

**Method:** `POST`

**Body:**

\```json
{
    "url": "http://example.com"
}
\```

**Response:**

\```json
{
    "url": "http://example.com",
    "is_safe": true
}
\```

### Reporting URLs

**Endpoint:** `/api/report_url`

**Method:** `POST`

**Body:**

\```json
{
    "url": "http://example.com",
    "report_type": "unsafe"  // or "safe"
}
\```

**Response:**

\```json
{
    "message": "URL report submitted successfully."
}
\```

### Example Usage

You can use tools like `curl` or Postman to interact with the API. Here's an example using `curl`:

\```bash
curl -X POST -H "Content-Type: application/json" -d '{"url": "http://example.com"}' http://localhost:5000/api/check_url
\```

## Contributions

Contributions to the Phishing Link Detector are welcome. Please fork the repository, make your changes, and submit a pull request.
