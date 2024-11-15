from flask import Flask, render_template, redirect, url_for

from lautomation import service, logger

app = Flask(__name__)


@app.route("/")
def index():
    # Obtém o status dos pinos e renderiza no template
    status = {int(pin.split('_')[1]): state for pin, state in service.get_status().items()}
    return render_template("index.html", status=status)

@app.route("/toggle/<int:pin>", methods=["POST"])
def toggle_pin(pin):
    # Alterna o estado do pino e redireciona para a página inicial
    current_status = service.get_status().get(f"relay_{pin}")
    new_action = "off" if current_status == "on" else "on"
    service.control_pin(pin, new_action)
    return redirect(url_for("index"))



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
