
class Clima:
    nombre = ""
    consigna_temp = 20.0
    consigna_hum_rel = 70
    

    def __init__(self, nombre):
        self.nombre = nombre

    def __init___(self, nombre, temp, hum, hum_suelo):
        self.nombre = nombre
        self.consigna_temp = temp
        self.consigna_hum_rel = hum
        self.consigna_humedad_suelo = hum_suelo

	
