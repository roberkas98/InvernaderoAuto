import RPi.GPIO as gpio

class Actuador:


    def __init__(self, id, pin):
        gpio.setmode(gpio.BOARD)
        gpio.setup(pin, gpio.OUT)
        self.id = id
        self.pin = pin


    def ActivarActuador(self):
        gpio.output(pin, True)

    def DesActivarActuador(self):
        gpio.output(pin, False)

        
