from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash
from classes.Dan_GPIO import FiveVoltChannel
from flask.ext.socketio import SocketIO, emit
import json
import time

app = Flask(__name__, static_url_path='/static')
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)
global relay

@app.route('/')
def home():
    return render_template("index.html", status="checked" if relay.is_on() else "", serverTime=int(time.time()))

@app.route('/updateClock')
def update_clock():
    print(time.time())
    return json.dumps({"currentTime": int(time.time())})

@socketio.on('changeStatus', namespace='/status')
def status_update(data):
    turn_on = True if data['lightSwitch'] == 1 else False
    relay.turn_on_5v_channel() if turn_on else relay.turn_off_5v_channel()
    emit('applyStatusUpdate', {"relayIsOn": relay.is_on()}, broadcast=True)

if __name__ == '__main__':
    global relay
    relay = FiveVoltChannel()
    socketio.run(app, host='0.0.0.0', port=80)



''' AJAX ROUTE
@app.route('/action', methods=['POST'])
def action():
    turn_on = True if request.form['lightSwitch'] == "1" else False
    relay.turn_on_5v_channel() if turn_on else relay.turn_off_5v_channel()
    return json.dumps({"relayIsOn": relay.is_on()})

@socketio.on('getStatusUpdate', namespace='/status')
def status_update():
    emit('applyStatusUpdate', {"relayIsOn": relay.is_on()}, broadcast=True)

@socketio.on('connect', namespace='/status')
def test_connect():
    print('Client connected')

@socketio.on('disconnect', namespace='/status')
def test_disconnect():
    print('Client disconnected')

'''