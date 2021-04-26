from Clima import Clima

class Invernadero:
    id = ""
    clima = Clima()
    frec_sampleo = 60 #segundos entre lecturas del sensor
    sensor_humedad_rel = SensorBMP280()
    sensor_temp = SensorBMP280()
    actuador_calentar = null
    actuador_enfriar = null
    actuador_riego = null
    actuador_ventilar = null



    def __init__(self, id):
        self.id=id

    def 