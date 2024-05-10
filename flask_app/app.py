from flask import Flask, render_template, request
import subprocess

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/configure", methods=["POST"])
def configure_wifi():
    body = request.json

    ssid = body["ssid"]
    password = body["password"]

    # Configure Wi-Fi
    subprocess.run(
        ["sudo", "wpa_passphrase", ssid, password],
        check=True,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    subprocess.run(
        ["sudo", "wpa_cli", "-i", "wlan0", "reconfigure"],
        check=True,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )

    return {"status": "success"}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
