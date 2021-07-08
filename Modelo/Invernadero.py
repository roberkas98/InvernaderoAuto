from Clima import Clima
from SensorBMP280 import SensorBMP280
from Actuador import Actuador
from AreaRiego import AreaRiego
from ModuloSensores import ModuloSensores

class Invernadero:
    id = 00
    nombre = ""
    clima = Clima
    frec_sampleo = 60 #segundos entre lecturas del sensor
    moduloSensores = ModuloSensores
    actuador_calentar = None
    actuador_ventilar = None
    actuador_humidificar = None
    AreasRiego = [AreaRiego]
    iluminacion = False
    actuador_iluminacion = Actuador
    horas_luz = 12



    def __init__(self, id):
        self.id=id

    def setTempSensor(self, SensorBMP280):
        self.sensor_temp=SensorBMP280

    def setActuadorEnfriar(self, Actuador):
        self.actuador_enfriar=Actuador

    def setClima(self, Clima):
        self.clima=Clima

    def RegularInvernadero(self):
        if(actuador_calentar == None and actuador_ventilar != None and actuador_humidicar == None):  #Caso 1 regulacion. 1 sensor temperatura/humedad 1 actuador ventilar
            temperatura, presion, humedad = self.sensor_temp.readBME280All()
            print(temperatura, presion, humedad)
            if(self.clima.max_temp<temperatura):
                self.actuador_ventilar.ActivarActuador()
            if(self.clima.hum_max<humedad and self.clima.temperatura_min<temperatura):
                self.actuador_ventilar.ActivarActuador()
        
        if(actuador_calentar == None and actuador_ventilar != None and actuador_humidicar != None): #Caso 2 regulacion. 1 sensor temperatura/humedad 1 actuador ventilar y 1 actuador humidificador 
            temperatura, presion, humedad = self.sensor_temp.readBME280All()
            print(temperatura, presion, humedad)
            if(self.clima.max_temp<temperatura):
                self.actuador_ventilar.ActivarActuador()
            if(self.clima.hum_max<humedad and self.clima.temperatura_min<temperatura):
                self.actuador_ventilar.ActivarActuador()
            if(self.clima.hum_min>humedad):
                self.actuador_humidificar.ActivarActuador()


        if(actuador_calentar != None and actuador_ventilar != None and actuador_humidicar != None): #Caso 3 regulacion. 1 sensor temperatura/humedad 1 actuador ventilar, 1 actuador humidificador, 1 calefactor
            temperatura, presion, humedad = self.sensor_temp.readBME280All()
            print(temperatura, presion, humedad)
            if(self.clima.max_temp<temperatura):
                self.actuador_ventilar.ActivarActuador()
            if(self.clima.min_temp>temperatura):
                self.actuador_calentar.ActivarActuador()
            if(self.clima.hum_max<humedad and self.clima.temperatura_min<temperatura):
                self.actuador_ventilar.ActivarActuador()
            if(self.clima.hum_min>humedad):
                self.actuador_humidificar.ActivarActuador()


        if(round(self.clima.consigna_temp)==round(temperatura)):
            self.actuador_calentar.DesactivarActuador()
        if(self.clima.consigna_hum>humedad and self.clima.temp_max>temperatura):
            self.actuador_ventilar.DesactivarActuador()
        if(self.clima.consigna_hum==humedad or self.clima.consigna_hum<humedad):
            self.actuador_humidificar.DesactivarActuador()

    def anadirAreaRiego(AreaRiego):
        self.AreasRiego.append(AreaRiego)

    def eliminarAreaRiego(id):
        for x in len(self.AreasRiego):
            if self.AreasRiego[x].id==id:
                AreasRiego.pop(x)

