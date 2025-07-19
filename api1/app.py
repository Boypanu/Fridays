from flask import Flask, jsonify
import requests
import logging

app = Flask(__name__)

# Setup logging
logging.basicConfig(level=logging.INFO)

API2_URL = "http://api2:5001/api2"

@app.route("/api_1", methods=["GET"])
def call_api2():
    app.logger.info("API1: Received request from user")
    try:
        response = requests.get(API2_URL)
        app.logger.info("API1: Called API2 successfully")
        return jsonify({
            "api1_message": "Hello from API_1 ",
            "api2_response": response.json()
        })
    except requests.exceptions.RequestException as e:
        app.logger.error(f"API1: Error calling API2: {e}")
        return jsonify({"error": "API2 is unreachable"}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
