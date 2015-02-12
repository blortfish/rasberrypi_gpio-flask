from datetime import datetime
import RPi.GPIO as GPIO
from Dan_GPIO import FiveVoltChannel
import time

relay = FiveVoltChannel()
relay.turn_off_5v_channel()
currentTime = datetime.now()
alarmTime = currentTime.replace(day=currentTime.day + 1, hour=6, minute=0, second=0, microsecond=0)
time.sleep(time.mktime(alarmTime.timetuple()) - time.mktime(currentTime.timetuple()))
relay.turn_on_5v_channel()