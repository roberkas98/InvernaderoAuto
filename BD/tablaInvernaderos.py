from BD import *
from Invernadero import *

class TablaInvernaderos():
    
    def AllInvernaderos():
        try:
            con = sql_connection()
            cursor = con.cursor('SELECT * FROM INVERNADEROS')
            invernaderos = cursor.fetchAll()
            return invernaderos
        except sqlite3.OperationalError as error:
	            print("Error al abrir:", error)

    def InsertInvernadero(invernadero):
        try:
            con = sql_connection()
            sentencia = 'INSERT INTO INVERNADEROS (ID, NOMBRE, CLIMA, ID_MODULO_SENSORES, ACTUADOR_CALENTAR, ACTUADOR_VENTILAR, ACTUADOR_HUMIDIFICAR, ILUMINACION, HORAS_LUZ) VALUES (?,?,?,?,?,?,?,?)'
            cursor = con.execute(sentencia, [invernadero.nombre, invernadero.clima.id, invernadero.moduloSensores.id, invernadero.actuadorCalentar.id, invernadero.actuador.actuadorVentilar.id, invernadero.actuadorHumidificar.id, invernadero.iluminacion, invernadero.horasLuz])
            con.commit()
            print("Guardado correctamente")
        except sqlite3.OperationalError as error:
	        print("Error al abrir:", error)