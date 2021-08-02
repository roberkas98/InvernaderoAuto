import sys
sys.path.append(".")
from BD import *
from tablaActuadores import TablaActuadores
from Actuador import *


#actuador = Actuador(14, 'actuador_12', 10)
#TablaActuadores.InsertActuador(actuador)
#actuadores = TablaActuadores.AllActuadores()
actuador1 = TablaActuadores.FindActuador("act")

print(actuador1)

