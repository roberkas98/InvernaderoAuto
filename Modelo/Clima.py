
class Clima:
    id = 00
    nombre = ""
    consigna_temp = 20.0
    max_temp = 22
    min_temp = 15
    consigna_hum_rel = 70
    hum_rel_min = 30
    hum_rel_max = 80
    

    def __init__(self, nombre):
        self.nombre = nombre

    def __init___(self, nombre, temp, hum, hum_suelo):
        self.nombre = nombre
        self.consigna_temp = temp
        self.consigna_hum_rel = hum
        self.consigna_humedad_suelo = hum_suelo

	
