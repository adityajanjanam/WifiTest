from flask import Flask, jsonify
import subprocess

app = Flask(__name__)

def get_wifi_details():
    result = subprocess.run(["netsh", "wlan", "show", "interfaces"], capture_output=True, text=True)
    if result.returncode == 0:
        return result.stdout
    return "Failed to retrieve WiFi details."

@app.route('/')
def home():
    return "<h1>Welcome to WiFi Test API</h1><p>Use /wifi to get WiFi details.</p>"

@app.route('/wifi', methods=['GET'])
def wifi():
    details = get_wifi_details()
    return jsonify({"wifi_details": details})

@app.route('/favicon.ico')
def favicon():
    return "", 204  # No Content

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
