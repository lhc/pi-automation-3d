from flask import Flask, jsonify, render_template
from lautomation import service, logger

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/pin/<int:pin>/on", methods=["GET"])
def turn_on(pin):
    response = service.control_pin(pin, "on")
    return jsonify(response), 200 if "relay" in response else 400

@app.route("/api/pin/<int:pin>/off", methods=["GET"])
def turn_off(pin):
    response = service.control_pin(pin, "off")
    return jsonify(response), 200 if "relay" in response else 400

@app.route("/api/status/", methods=["GET"])
def get_status():
    response = service.get_status()
    return jsonify(response), 200

if __name__ == "__main__":
    logger.log_info("Starting Flask application")
    app.run(host="0.0.0.0", port=5000, debug=True)
