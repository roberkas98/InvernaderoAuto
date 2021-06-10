from Clima import Clima
from Actuador import Actuador

class AreaRiego:
    id = ""
    sensorHumedad_1 = Sensor()
    sensorHumedad_2 = SensorBMP280()
    actuadorRiego = Actuador()
    consigna_humedad_suelo = 70
    tipo_riego = 0 #Se implementara mas adelante
    #implmentar riego temprizado


    def __init__(self, id):
        self.id=id

    def setSensor1(Sensor):
        self.sensorHumedad_1=Sensor()

    def setSensor2(Sensor):
        self.sensorHumedad_1=Sensor()


    def setActuadorRiego(Actuador):
        self.actuadorRiego=Actuador()
