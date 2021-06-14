from Clima import Clima
from SensorBMP280 import SensorBMP280
from Actuador import Actuador
from AreaRiego import AreaRiego

class Invernadero:
    id = ""
    clima = Clima
    frec_sampleo = 60 #segundos entre lecturas del sensor
    sensor_humedad_rel = SensorBMP280
    sensor_temp = SensorBMP280
    #actuador_calentar = null
    actuador_enfriar = Actuador
    #actuador_ventilar = null
    AreasRiego = [AreaRiego]



    def __init__(self, id):
        self.id=id

    def setTempSensor(self, SensorBMP280):
        self.sensor_temp=SensorBMP280

    def setActuadorEnfriar(self, Actuador):
        self.actuador_enfriar=Actuador

    def setClima(self, Clima):
        self.clima=Clima

    def RegularInvernadero(self):
		
        temperatura, presion, humedad = self.sensor_temp.readBME280All()
        print(temperatura, presion, humedad)
        if(self.clima.consigna_temp<temperatura+1):
            self.actuador_enfriar.ActivarActuador()
        if(self.clima.consigna_temp>temperatura-1):
             #self.actuador_calentar.ActivarActuador()
             pass
        if(round(self.clima.consigna_temp)==round(temperatura)):
            self.actuador_enfriar.DesactivarActuador()
            self.actuador_calentar.DesactivarActuador()
