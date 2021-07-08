from Clima import Clima
from Actuador import Actuador
from Sensor import Sensor
from SensorBMP280 import SensorBMP280


class AreaRiego:
    id = 00
    nombre = ""
    sensorHumedad_1 = Sensor
    sensorHumedad_2 = Sensor
    actuadorRiego = Actuador
    consigna_humedad_suelo = 70
    tipo_riego = 0 #Se implementara mas adelante
    #implmentar riego temprizado


    def __init__(self, id):
        self.id=id

    def setSensorMaster(Sensor):
        self.sensorHumedad_1=Sensor

    def setSensorSlave(Sensor):
        self.sensorHumedad_2=Sensor


    def setActuadorRiego(Actuador):
        self.actuadorRiego=Actuador()

    def regar():
        self.actuadorRiego