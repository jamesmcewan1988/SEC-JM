from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)
SEC_API_KEY = os.getenv("SEC_API_KEY")  # Use environment variable

@app.route("/query")
def query():
    q = request.args.get("q")
    if not q:
        return {"error": "Missing query"}, 400
    url = f"https://api.sec-api.io?token={SEC_API_KEY}&q={q}"
    response = requests.get(url)
    return jsonify(response.json())
