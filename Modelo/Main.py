from Actuador import Actuador
from Invernadero import Invernadero
from Clima import Clima
from Regulador import Regulador
from SensorBMP280 import SensorBMP280


sensor = SensorBMP280("sensor1", 2)
actuador = Actuador("enfriador", 21)
clima = clima("seco")
invernadero = Invernadero("Prueba")
invernadero.setActuadorEnfriar(actuador)
invernadero.setClima(clima)
while(true):
    Regulador.RegularInvernadero(invernadero)
    sleep(3)


