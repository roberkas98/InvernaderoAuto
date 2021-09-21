import sys
sys.path.append(".")
from BD import *
from tablaActuadores import TablaActuadores
from Actuador import *


actuador = Actuador(53, 'calderon', 10)
TablaActuadores.InsertActuador(actuador)
actuadores = TablaActuadores.AllActuadores()
print(actuadores)
actuador1 = TablaActuadores.FindActuadorByNombre("calde")

print(actuador1)

