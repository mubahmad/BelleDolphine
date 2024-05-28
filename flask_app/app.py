from flask import Flask, json, render_template, request
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
                "wlan1",
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


@app.route("/api/state-of-op", methods=["GET", "POST"])
def current_state_of_op():
    if request.method == "GET":
        with open("../state.json", "r") as file:
            return json.loads("".join(file.readlines()))
    if request.method == "POST":
        body = request.json
        new_state_of_op = body["newState"]
        with open("../state.json", "w") as file:
            file.write(json.dumps({"currentStateOfOperation": new_state_of_op}))
        return {"currentStateOfOperation": new_state_of_op}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
