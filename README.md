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