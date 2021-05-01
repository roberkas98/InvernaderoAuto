import OPi.GPIO as gpio

class Actuador:

    estado = false

    def __init__(self, id, pin):
        #añadir  restricciones de rwepeticion de pines
        self.id = id
        self.pin = pin
        gpio.setbopard(PC2)
        gpio.setmode(gpio.BOARD)
        gpio.setup(pin, gpio.OUT)



    def ActivarActuador(self):
        self.estado=True
        gpio.output(pin, gpio.HIGH)

    def DesactivarActuador(self):
        self.estado=False
        gpio.output(pin, gpio.LOW)

