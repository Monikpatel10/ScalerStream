from flask import Flask
from flask_socketio import SocketIO
import redis

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")
r = redis.Redis(host='localhost', port=6379, db=0)

@app.route('/')
def index():
    return "ScalerStream backend is running."

@socketio.on('connect')
def handle_connect():
    print('Client connected')
    while True:
        log = r.lpop('logs')
        if log:
            socketio.emit('log', log.decode('utf-8'))
        socketio.sleep(1)

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000)
from flask_socketio import SocketIO
import redis

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")
r = redis.Redis(host='localhost', port=6379, db=0)

@app.route('/')
def index():
    return "ScalerStream backend is running."

@socketio.on('connect')
def handle_connect():
    print('Client connected')
    while True:
        log = r.lpop('logs')
        if log:
            socketio.emit('log', log.decode('utf-8'))
        socketio.sleep(1)

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000)
from flask import Flask
from flask_socketio import SocketIO
import redis

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")
r = redis.Redis(host='localhost', port=6379, db=0)

@app.route('/')
def index():
    return "ScalerStream backend is running."

@socketio.on('connect')
def handle_connect():
    print('Client connected')
    while True:
        log = r.lpop('logs')
        if log:
            socketio.emit('log', log.decode('utf-8'))
        socketio.sleep(1)

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000)
# Entry point for Flask app
from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/')
def index():
    return "ScalerStream API running"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
