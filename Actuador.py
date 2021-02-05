import RPi.GPIO as gpio

class Actuador:

    estado = false

    def __init__(self, id, pin):
        gpio.setmode(gpio.BOARD)
        gpio.setup(pin, gpio.OUT)
        self.id = id
        self.pin = pin



    def ActivarActuador(self):
        gpio.output(pin, True)
        self.estado=True

    def DesactivarActuador(self):
        gpio.output(pin, False)
        self.estado=False
