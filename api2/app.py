from flask import Flask, jsonify
import logging

app = Flask(__name__)

# Setup logging
logging.basicConfig(level=logging.INFO)

@app.route("/api2", methods=["GET"])
def api2_response():
    app.logger.info("API2: Received request from API1")
    return jsonify({"api2_message": "Hello from API_2"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
