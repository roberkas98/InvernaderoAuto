import RPi.GPIO as gpio


class Sensor:


    def __init__(self, id, pin):
        self.id = id
        self.pin = pin

