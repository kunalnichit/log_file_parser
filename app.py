from flask import Flask, request, jsonify
import re
import pandas as pd
from collections import Counter

app = Flask(__name__)

@app.get('/test-api')
def test_api():
    return jsonify({"message":"Hello World"})

@app.post('/parse-log')
def log_file_parser():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"Error":"Invalid JSON payload"}), 400

        file_path = data.get("file")
        top_n = data.get("top_n",3)

        if not file_path.endswith(".log"):
            return jsonify({"Error": "Only required .log file format"}), 400

        with open(file_path,"r", encoding='utf-8') as f:
            log_content = f.read()

        # print(log_content)
        lines = log_content.strip().split('\n')
        parsed_data = []

        LOG_PATTERN = r"(?P<timestamp>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) (?P<level>[A-Z]+) (?P<message>.+)"

        for line in lines:
            match = re.match(LOG_PATTERN,line)
            if match:
                parsed_data.append(match.groupdict())

        print(parsed_data)
        df = pd.DataFrame(parsed_data)

        level_counts = df["level"].value_counts().to_dict()
        print(level_counts)

        error_message = df[df["level"]=="ERROR"]["message"].to_list()
        counter = Counter(error_message)
        most_common = counter.most_common(top_n)
        error_count = dict(most_common)
        print(error_count)

        extra={}

        if df["timestamp"].notna().any():
            extra["time_range"] = [df["timestamp"].min(),df["timestamp"].max()]

        extra['login_count'] = int(df["message"].str.contains("logged in", case=False, na=False).sum())
        extra['logout_count'] = int(df["message"].str.contains("logged out", case=False, na=False).sum())

        insights = {
            "level_counts":level_counts,
            "error_counts":error_count,
            "extra_insights":extra
        }

        return jsonify(insights), 200
    
    except Exception as e:
        return jsonify({"Error":str(e)}), 500


if __name__=='__main__':
    app.run(debug=True, host="0.0.0.0")