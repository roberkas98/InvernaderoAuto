class Invernadero:
    id = ""
    consigna_temp = 20.0
    consigna_hum_rel = 70
    consigna_humedad_suelo = 70
    tipo_riego = 0 //Se implementara mas adelante
    frec_sampleo = 60 #segundos entre lecturas del sensor
    sensor_humedad_rel = SensorBMP280
    sensor_temp = SensorBMP280
    actuador_calentar = null
    actuador_enfriar = null
    actuador_riego = null
    actuador_ventilar = null



    def __init__(self, id):
        self.id=id
