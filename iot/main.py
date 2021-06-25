import sys
from flask import Flask, jsonify
import pathlib
firmware_path = str(pathlib.Path('../firmware').resolve())
sys.path.append(firmware_path)
import time
from Client import udpsend

app = Flask(__name__)
udp = udpsend(34512, SrcIP = '127.0.0.1')

@ app.route('/pump/on')
def on():
    #udp.pump(1)
    return jsonify({"ok": True}), 200

@ app.route('/pump/off')
def off():
    #udp.pump(0)
    return jsonify({"ok": True}), 200

if __name__ == '__main__':
    app.run(port=8081, debug=True)

