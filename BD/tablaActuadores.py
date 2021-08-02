from BD import *
import sys
sys.path.append('./Modelo')
from Actuador import *

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
           BD.sql_con_close(con)

    def FindActuadorByNombre(nombre):
        try:
            con = BD.sql_connection()
            sentencia = "SELECT * FROM actuadores WHERE nombre LIKE ?;"  
            cursor = con.cursor()
            cursor.execute(sentencia, ["%" + nombre + "%"]) #Los porcentajes de la expresion regular hay que ponerlos aqui, ya que sino no detecta el placeholder de la interrogacion y da error
            actuadores = cursor.fetchall()
            return actuadores
        except sqlite3.OperationalError as error:
            print("Error al abrir:", error)
        finally:
            BD.sql_con_close(con)

    def FindActuadorById(id):
        try:
            con = BD.sql_connection()
            sentencia = "SELECT * FROM actuadores WHERE id LIKE ?;"  
            cursor = con.cursor()
            cursor.execute(sentencia, ["%" + id + "%"]) #Los porcentajes de la expresion regular hay que ponerlos aqui, ya que sino no detecta el placeholder de la interrogacion y da error
            actuadores = cursor.fetchall()
            return actuadores
        except sqlite3.OperationalError as error:
            print("Error al abrir:", error)
        finally:
            BD.sql_con_close(con)


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
            BD.sql_con_close(con)

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

