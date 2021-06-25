import sys
from flask import Flask, jsonify
import time
import subprocess as sp

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({"ok": True}), 200


@ app.route('/led/<RGB>')
def led(RGB='0xffffff'):
    red = int(RGB[:2], 16)
    green = int(RGB[2:4], 16)
    blue = int(RGB[4:], 16)
    cmd = ' '.join(["python3", "Client.py", str(red), str(green), str(blue)])
    sp.run(cmd, shell=True)    
    print(cmd)
    return jsonify({"ok": True, "red":red, "green":green, "blue":blue}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081, debug=True)

