from flask import Flask, make_response, request, render_template, send_file, abort, jsonify, send_from_directory
from flask import Response
import io
import csv
import os
import json

app = Flask(__name__, static_url_path="", static_folder='/home/ach4l/mysite')
#app = Flask(__name__, static_url_path="/static", static_folder='/home/ach4l/mysite/src')

from flask import make_response

@app.route('/manifest')
def manifest():
    with open('/manifest.webapp') as f:
        data = json.load(f)
    res = make_response(data, 200)
    print(data)
    res.headers["Content-Type"] = "application/x-web-app-manifest+json"
    return res


@app.route("/")
def hello():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001, debug=True)