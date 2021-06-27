import sys
from flask import Flask, jsonify
import time
import subprocess as sp

app = Flask(__name__)
port = 8081

ip = '127.0.0.1'
page = f'<a href= "http://{ip}:{port}/led/000000">消灯</a> <br>\n\
<a href="http://{ip}:{port}/led/ffffff">白</a><br>\n\
<a href="http://{ip}:{port}/led/ff00000">赤</a><br>\n\
<a href="http://{ip}:{port}/led/00ff00">緑</a><br>\n\
<a href="http://{ip}:{port}/led/0000ff">青</a><br>\n\
<a href="http://{ip}:{port}/led/6f00ff">紫</a><br>\n\
<a href="http://{ip}:{port}/led/ffd400">黄</a><br>\n\
<a href="http://{ip}:{port}/led/afdfe4">水</a><br>\n\
<a href="http://{ip}:{port}/led/f15a22">橙</a><br>'

@app.route('/')
def index():
    return page

@ app.route('/led/<RGB>')
def led(RGB='0xffffff'):
    red = int(RGB[:2], 16)
    green = int(RGB[2:4], 16)
    blue = int(RGB[4:], 16)
    cmd = ' '.join(["python3", "Client.py", str(red), str(green), str(blue)])
    sp.run(cmd, shell=True)    
    print(cmd)
    return f'<font color="#{RGB}">この色にしました</font><br>\n' + page

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port, debug=False)
