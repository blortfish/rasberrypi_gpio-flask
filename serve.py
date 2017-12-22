from flask import Flask, render_template
from utils.FiveVoltChannel import FiveVoltChannel
from flask_socketio import SocketIO, emit

# app = Flask(__name__, static_url_path='/static')
# socketio = SocketIO(app)
# socketio.run(app, debug=True)
app = Flask(__name__)

socketio = SocketIO(app)


@app.route('/')
def index():
    relay = FiveVoltChannel()
    return render_template("index.html", status="checked" if relay.is_on() else "")


@socketio.on('changeStatus')
def status_update(data):
    emit('applyStatusUpdate', {"relayIsOn": True if data['lightSwitch'] == 1 else False}, broadcast=True)


socketio.run(app)