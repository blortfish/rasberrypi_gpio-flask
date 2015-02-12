from datetime import datetime
import RPi.GPIO as GPIO
import time


def prepare_5v_rail():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(11, GPIO.OUT)


def release_5v_rail():
    GPIO.cleanup()

prepare_5v_rail()

for i in range(0, 10):
    time.sleep(.05)
    GPIO.output(11, True)
    time.sleep(.05)
    GPIO.output(11, False)

release_5v_rail()