import RPi.GPIO as gpio


class Sensor:


    def __init__(self, id, pin):
        id = ""
        consigna_temp = 20.0
        consigna_hum_rel = 70
        consigna_humedad_suelo = 70
        tipo_riego = 0 //Se implementara mas adelante
        frec_sampleo = 60 #segundos entre lecturas del sensor
