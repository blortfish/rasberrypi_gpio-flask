import utils.mock.MockGPIO as GPIO


class FiveVoltChannel:
    def __init__(self):
        self.prepare_5v_channel()

    def prepare_5v_channel(self):
        GPIO.cleanup()
        GPIO.setmode(GPIO.BOARD)

    def is_on(self):
        return GPIO.IS_ON

    def turn_on_5v_channel(self):
        GPIO.output(11, True)

    def turn_off_5v_channel(self):
        GPIO.output(11, False)

    def run_cleanup(self):
        GPIO.cleanup()
