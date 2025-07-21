from flask import Flask, jsonify, request
import logging

app = Flask(__name__)

# Setup logging
logging.basicConfig(level=logging.INFO)

@app.route("/api2", methods=["GET", "POST"])
def api2_response():
    if request.method == "GET":
        app.logger.info("API2: Received GET request from API1")
        return jsonify({"api2_message": "Hello from API_2 (GET)"})
    
    if request.method == "POST":
        data = request.get_json()
        app.logger.info(f"API2: Received POST data: {data}")
        return jsonify({
            "api2_message": "Hello from API_2 (POST)",
            "received_data": data
        })

@app.route("/health", methods=["GET"])
def health():
    return {"status": "ok"}, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
