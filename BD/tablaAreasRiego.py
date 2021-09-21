from BD import *
import sys
sys.path.append('./Modelo')
from AreaRiego import *

class TablaAreasRiego():
    
    def AllActuadores():
        try:
            con = BD.sql_connection()
            sentencia = "SELECT * FROM areasRiego;"
            cursor = con.cursor()
            cursor.execute(sentencia)
            areasRiego = cursor.fetchall()
            return areasRiego
        except sqlite3.OperationalError as error:
            print("Error al abrir:", error)
        finally:
           BD.sql_con_close(con)

    def FindAreaRiegoByNombre(nombre):
        try:
            con = BD.sql_connection()
            sentencia = "SELECT * FROM areasRiego WHERE nombre LIKE ?;"  
            cursor = con.cursor()
            cursor.execute(sentencia, ["%" + nombre + "%"]) #Los porcentajes de la expresion regular hay que ponerlos aqui, ya que sino no detecta el placeholder de la interrogacion y da error
            actuadores = cursor.fetchall()
            return actuadores
        except sqlite3.OperationalError as error:
            print("Error al abrir:", error)
        finally:
            BD.sql_con_close(con)

    def FindAreaRiegoById(id):
        try:
            con = BD.sql_connection()
            sentencia = "SELECT * FROM areasRiego WHERE id LIKE ?;"  
            cursor = con.cursor()
            cursor.execute(sentencia, ["%" + id + "%"]) #Los porcentajes de la expresion regular hay que ponerlos aqui, ya que sino no detecta el placeholder de la interrogacion y da error
            areasRiego = cursor.fetchall()
            return areasRiego
        except sqlite3.OperationalError as error:
            print("Error al abrir:", error)
        finally:
            BD.sql_con_close(con)


    def InsertAreaRiego(areaRiego):
        try:
            con = BD.sql_connection()
            sentencia = "INSERT INTO areasRiego (ID, NOMBRE, sensorHumedadMaster, sensorHumedadEsclavo, actuadorRiego, consignaHumedadsSuelo, tipoRiego ) VALUES (?,?,?,?,?,?,?)"
            cursor = con.execute(sentencia, [areaRiego.id, areaRiego.nombre, areaRiego.pin, areaRiego.sensorHumedadMaster, areaRiego.sensorHumedadEsclavo, areaRiego.actuadorRiego, areaRiego.consignaHumedadsSuelo , areaRiego.tipoRiego])
            con.commit()
            print("Guardado correctamente")
        except sqlite3.OperationalError as error:
	        print("Error al abrir:", error)
        finally:
            BD.sql_con_close(con)

    def UpdateAreaRiego(areaRiego):
        try:
            con = BD.sql_connection()
            sentencia = "UPDATE actuadores SET NOMBRE=?, PIN=? WHERE ID=?"
            cursor = con.execute(sentencia,[areaRiego.id, areaRiego.nombre, areaRiego.pin, areaRiego.sensorHumedadMaster, areaRiego.sensorHumedadEsclavo, areaRiego.actuadorRiego, areaRiego.consignaHumedadsSuelo , areaRiego.tipoRiego])
            con.commit()
            print("Actualizado correctamente")
        except sqlite3.OperationalError as error:
	        print("Error al abrir:", error)
        finally:
            BD.sql_con_close()

    def DeleteAreaRiego(areaRiego):
        try:
            con = BD.sql_connection()
            sentencia = "DELETE FROM areasRiego WHERE ID=?"
            cursor = con.execute(sentencia, areaRiego.id)
            con.commit()
            print("Borrado correctamente")
        except sqlite3.OperationalError as error:
	        print("Error al abrir:", error)
        finally:
            BD.sql_con_close()

    def DeleteActuador(id):
        try:
            con = BD.sql_connection()
            sentencia = "DELETE FROM areasRiego WHERE ID=?"
            cursor = con.execute(sentencia, id)
            con.commit()
            print("Borrado correctamente")
        except sqlite3.OperationalError as error:
	        print("Error al abrir:", error)
        finally:
            BD.sql_con_close()

