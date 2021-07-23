from BD import *
from Modelo.Actuador import *

class TablaActuadores(BD):
    
    def AllActuadores():
        try:
            con = BD.sql_connection()
            sentencia = "SELECT * FROM actuadores;"
            cursor = con.cursor()
            cursor.execute(sentencia)
            actuadores = cursor.fetchall()
            return actuadores
        except sqlite3.OperationalError as error:
            print("Error al abrir:", error)
        finally:
            BD.sql_con_close()

    def FindActuador():


    def InsertActuador(actuador):
        try:
            con = BD.sql_connection()
            sentencia = "INSERT INTO actuadores (ID, NOMBRE, PIN) VALUES (?,?,?)"
            cursor = con.execute(sentencia, [actuador.id, actuador.nombre, actuador.pin])
            con.commit()
            print("Guardado correctamente")
        except sqlite3.OperationalError as error:
	        print("Error al abrir:", error)
        finally:
            BD.sql_con_close()

    def UpdateActuador(actuador):
        try:
            con = BD.sql_connection()
            sentencia = "UPDATE actuadores SET NOMBRE=?, PIN=? WHERE ID=?"
            cursor = con.execute(sentencia, [actuador.nombre, actuador.pin, actuador.id])
            con.commit()
            print("Actualizado correctamente")
        except sqlite3.OperationalError as error:
	        print("Error al abrir:", error)
        finally:
            BD.sql_con_close()

    def DeleteActuador(actuador):
        try:
            con = BD.sql_connection()
            sentencia = "DELETE FROM actuadores WHERE ID=?"
            cursor = con.execute(sentencia, actuador.id)
            con.commit()
            print("Borrado correctamente")
        except sqlite3.OperationalError as error:
	        print("Error al abrir:", error)
        finally:
            BD.sql_con_close()

    def DeleteActuador(id):
        try:
            con = BD.sql_connection()
            sentencia = "DELETE FROM actuadores WHERE ID=?"
            cursor = con.execute(sentencia, id)
            con.commit()
            print("Borrado correctamente")
        except sqlite3.OperationalError as error:
	        print("Error al abrir:", error)
        finally:
            BD.sql_con_close()

