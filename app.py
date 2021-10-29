from flask import Flask, render_template, redirect, request, flash, session, jsonify
import requests
import json

app = Flask(__name__)
app.secret_key = 'LISTENER'

@app.route('/listening', methods=['POST'])
def receive_callback():

    callback = request.data
    callback_json = json.loads(callback)
    print(type(callback_json))
    print('received new action: ', callback_json['action'])
    callback_str = json.dumps(callback_json)
    f = open('data.json', 'a')
    f.write(callback_str)
    f.close
    print('new payload recorded')

    data = {"status": "logged", "code": 200}
    resp = jsonify(data)
    resp.status_code = 200
    return resp

if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0')
