import OPi.GPIO as gpio


class Actuador:

    estado = False

    def __init__(self, id, pin):
        #anadir  restricciones de rwepeticion de pines
        self.id = id
        self.pin = pin
        gpio.setboard(gpio.PC2)
        gpio.setmode(gpio.BCM)
        gpio.setup(pin, gpio.OUT)



    def ActivarActuador(self):
        self.estado=True
        gpio.output(self.pin, gpio.LOW)
        print("Se ha ha activado el " + self.id)

    def DesactivarActuador(self):
        self.estado=False
        gpio.output(self.pin, gpio.HIGH)
        print("Se ha ha desactivado el %s", self.id)

