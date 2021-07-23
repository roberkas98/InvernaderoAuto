import sys
from BD import *
from tablaActuadores import TablaActuadores
from Modelo.Actuador import *

sys.path.append("..")

actuador = Actuador(11, 'actuador_1', 10)
TablaActuadores.InsertActuador(actuador)
actuadores = TablaActuadores.AllActuadores()
print(actuadores)

