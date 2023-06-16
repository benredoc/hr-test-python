from flask import Flask, jsonify, request
import time

app = Flask(__name__)

@app.route('/timestamp')
def timestamp():
    current_timestamp = int(time.time())
    return jsonify(timestamp=current_timestamp)

@app.route('/readdata', methods=['POST'])
def readdata():
    data = request.get_json()
    return jsonify(data)

if __name__ == '__main__':
    app.run()
