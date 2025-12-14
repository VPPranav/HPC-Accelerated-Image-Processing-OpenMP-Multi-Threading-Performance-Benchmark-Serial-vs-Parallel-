from flask import Flask, render_template, jsonify
import json
import os

app = Flask(__name__)

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
LOG_DIR = os.path.join(BASE_DIR, "results", "logs")

def load_json(filename):
    path = os.path.join(LOG_DIR, filename)
    if not os.path.exists(path):
        return {}
    with open(path, "r") as f:
        return json.load(f)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/serial")
def serial_metrics():
    return jsonify(load_json("serial_metrics.json"))

@app.route("/api/parallel")
def parallel_metrics():
    return jsonify(load_json("parallel_metrics.json"))

@app.route("/api/compare")
def compare_metrics():
    return jsonify(load_json("compare_metrics.json"))

if __name__ == "__main__":
    app.run(debug=True)
