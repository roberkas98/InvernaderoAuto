from Actuador import Actuador
from Invernadero import Invernadero
from Clima import Clima
from SensorBMP280 import SensorBMP280
import time


sensor = SensorBMP280("sensor1", 2)
actuador = Actuador("enfriador", 21)
clima = Clima("seco")
clima.consigna_temp = 29.0
invernadero = Invernadero("Prueba")
invernadero.setTempSensor(sensor)
invernadero.setActuadorEnfriar(actuador)
invernadero.setClima(clima)
while(True):
	invernadero.RegularInvernadero()
	time.sleep(3)
	


