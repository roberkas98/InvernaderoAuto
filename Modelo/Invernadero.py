from Clima import Clima
from SensorBMP280 import SensorBMP280
from Actuador import Actuador
from AreaRiego import AreaRiego

class Invernadero:
    id = ""
    clima = Clima()
    frec_sampleo = 60 #segundos entre lecturas del sensor
    sensor_humedad_rel = SensorBMP280()
    sensor_temp = SensorBMP280()
    actuador_calentar = null
    actuador_enfriar = Actuador()
    actuador_ventilar = null
    AreasRiego = [AreaRiego()]



    def __init__(self, id):
        self.id=id

    def setTempSensor(SensorBMP280):
        self.sensor_temp=SensorBMP280()

    def setActuadorEnfriar(Actuador):
        self.actuador_enfriar=Actuador()

    def setClima(Clima):
        self.clima=Clima()

    def RegularInvernadero(invernadero):
        temperatura, presion, humedad = invernadero.sensor_temp.readBME280All()
        if(invernadero.consigna_temp>temperatura+1):
            invernadero.actuador_enfriar.ActivarActuador()
        if(invernadero.consigna_temp<temperatura-1):
            invernadero.actuador_calentar.ActivarActuador()
        if(round(invernadero.consigna_temp)==round(temperatura)):
            invernadero.actuador_enfriar.DesactivarActuador()
            invernadero.actuador_calentar.DesactivarActuador()