## Log File Parser (Flask API + Pandas)

Simple Flask api, which can get log file from user and parse that log file such as log level counts(INFO, WARN, ERROR, DEBUG), login-logout counts and some extra insights


# Quickstart

-- clone project
-- python -m venv venv
-- .\venv\Scripts\activate
-- pip install -r requirements.txt
-- run command 
    python app.py

# endpoints

GET - '/test-api'(Hello World)
POST - '/parse-log'(log parser api)

# log file format

YYYY-MM-DD HH-MM-SS LEVEL message...

# sample output

{
  "error_counts": {
    "Disk space low": 2,
    "Disk write failed": 2,
    "Failed to connect to database": 1
  },
  "extra_insights": {
    "login_count": 3,
    "logout_count": 3,
    "time_range": [
      "2025-08-27 10:15:22",
      "2025-08-27 10:50:00"
    ]
  },
  "level_counts": {
    "DEBUG": 1,
    "ERROR": 5,
    "INFO": 6,
    "WARN": 2
  }
}