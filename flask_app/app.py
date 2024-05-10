from flask import Flask, render_template, request
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/configure', methods=['POST'])
def configure_wifi():
    ssid = request.form['ssid']
    password = request.form['password']
    
    # Configure Wi-Fi
    subprocess.run(['sudo', 'wpa_passphrase', ssid, password], check=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    subprocess.run(['sudo', 'wpa_cli', '-i', 'wlan0', 'reconfigure'], check=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    return 'Wi-Fi configured successfully.'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
