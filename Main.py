class Main:


invernaderos = []

    def RegularInvernadero(invernadero):
        temperatura, presion, humedad = invernadero.sensor_temp.readBME280All()
        if(invernadero.consigna_temp>temperatura+1):
            invernadero.actuador_enfriar.ActivarActuador()
        if(invernadero.consigna_temp<temperatura-1):
            invernadero.actuador_calentar.ActivarActuador()
        if(round(invernadero.consigna_temp)==round(temperatura):
            invernadero.actuador_enfriar.DesactivarActuador()
            invernadero.actuador_calentar.DesactivarActuador()
        if()





#
