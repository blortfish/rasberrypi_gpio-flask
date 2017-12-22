BOARD = 1
OUT = 1
IS_ON = False

def setmode(*args):
    pass


def setup(*args):
    pass


def output(pin, value):
    global IS_ON
    IS_ON = value


def cleanup():
    pass


def input(*args):
    return 1

