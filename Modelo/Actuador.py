#import OPi.GPIO as gpio


class Actuador:

    id = 00
    nombre = ""
    pin = 00
    estado = False

    def __init__(self, id, nombre, pin):
        #anadir  restricciones de rwepeticion de pines
        self.id = id
        self.nombre = nombre
        self.pin = pin
        #gpio.setboard(gpio.PC2) #Hay que cambiarlo si migramos a otra placa
        #gpio.setmode(gpio.BCM) #Define como nos refermos a los pines de la placa
        #gpio.setup(pin, gpio.OUT)



    def ActivarActuador(self):
        self.estado=True
        #gpio.output(self.pin, gpio.LOW)
        print("Se ha ha activado el " + self.id)

    def DesactivarActuador(self):
        self.estado=False
        #gpio.output(self.pin, gpio.HIGH)
        print("Se ha ha desactivado el %s", self.id)

