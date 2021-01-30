import RPi.GPIO as gpio

class Sensor:


    def __init__(self, id, pin):
        gpio.setmode(gpio.BOARD)
        gpio.setup(pin, gpio.IN)
        self.id = id
        self.pin = pin
