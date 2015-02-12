from datetime import datetime
import RPi.GPIO as GPIO
import time


class FiveVoltChannel:

    def __init__(self):
        #  currentTime = datetime.now()
        #  alarmTime = currentTime.replace(day=currentTime.day + 1, hour=6, minute=50, second=0, microsecond=0)
        #  time.sleep(time.mktime(alarmTime.timetuple()) - time.mktime(currentTime.timetuple()))
        self.prepare_5v_channel(self)

    @staticmethod
    def is_off():
        return GPIO.input(11) == 0

    @staticmethod
    def is_on():
        return not GPIO.input(11) == 0

    @staticmethod
    def prepare_5v_channel(self):
        self.run_cleanup()
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(11, GPIO.OUT)

    @staticmethod
    def turn_on_5v_channel():
        GPIO.output(11, True)

    @staticmethod
    def turn_off_5v_channel():
        GPIO.output(11, False)

    @staticmethod
    def run_cleanup():
        GPIO.cleanup()
