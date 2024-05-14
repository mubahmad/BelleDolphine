from flask import Flask, render_template, request
import subprocess

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/configure", methods=["POST", "GET"])
def configure_wifi():
    if request.method == "POST":
        body = request.json

        ssid = body["ssid"]
        password = body["password"]

        # Configure Wi-Fi
        subprocess.run(
            [
                "sudo",
                "nmcli",
                "device",
                "wifi",
                "connect",
                ssid,
                "ifname",
                "wlan0",
                "password",
                password,
            ],
            check=True,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )

        return {"status": "success"}
    if request.method == "GET":
        print(subprocess.check_output("netsh wlan show interfaces").decode())
        return {"status": "success"}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
