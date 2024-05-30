from flask import Flask
from flask import json
import datetime

app = Flask(__name__)

uptime = f"up since {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
version="0.0.1"

@app.route("/")
def main():
    return "Hello! ToBCloud"

@app.route("/healthz")
def health():
    ret={
        "status": "OK",
        "version": version,
        "uptime": uptime
    }
    return json.dumps(ret)

if __name__ == "__main__":
    app.run("0.0.0.0",port=80)
