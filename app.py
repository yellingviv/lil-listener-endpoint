from flask import Flask, render_template, redirect, request, flash, session, jsonify
import requests
import json

app = Flask(__name__)
app.secret_key = 'LISTENER'

@app.route('/listening', methods=['POST'])
def receive_callback():

    callback = request.data
    callback_json = json.loads(callback)
    callback_parsed = dict(callback_json)
    print(callback_parsed)

if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0')
