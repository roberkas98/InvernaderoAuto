from BD import *
import sys
sys.path.append('./Modelo')
from Clima import *

class TablaClima():
    
    def AllClimas():
        try:
            con = BD.sql_connection()
            sentencia = "SELECT * FROM climas;"
            cursor = con.cursor()
            cursor.execute(sentencia)
            climas = cursor.fetchall()
            return climas
        except sqlite3.OperationalError as error:
            print("Error al abrir:", error)
        finally:
           BD.sql_con_close(con)

    def FindClimaByNombre(nombre):
        try:
            con = BD.sql_connection()
            sentencia = "SELECT * FROM climas WHERE nombre LIKE ?;"  
            cursor = con.cursor()
            cursor.execute(sentencia, ["%" + nombre + "%"]) #Los porcentajes de la expresion regular hay que ponerlos aqui, ya que sino no detecta el placeholder de la interrogacion y da error
            climas = cursor.fetchall()
            return climas
        except sqlite3.OperationalError as error:
            print("Error al abrir:", error)
        finally:
            BD.sql_con_close(con)

    def FindClimaById(id):
        try:
            con = BD.sql_connection()
            sentencia = "SELECT * FROM actuadores WHERE id LIKE ?;"  
            cursor = con.cursor()
            cursor.execute(sentencia, ["%" + id + "%"]) #Los porcentajes de la expresion regular hay que ponerlos aqui, ya que sino no detecta el placeholder de la interrogacion y da error
            climas = cursor.fetchall()
            return climas
        except sqlite3.OperationalError as error:
            print("Error al abrir:", error)
        finally:
            BD.sql_con_close(con)


    def InsertClima(clima):
        try:
            con = BD.sql_connection()
            sentencia = "INSERT INTO actuadores (ID, NOMBRE, CONSIGNA_TEMP, MAX_TEMP, MIN_TEMP, CONSIGNA_HUM_REL, HUM_REL_MIN, HUM_REAL_MAX) VALUES (?,?,?,?,?,?,?,?)"
            cursor = con.execute(sentencia, [clima.id, clima.nombre, clima.consigna_temp, clima.max_temp, clima.min_temp, consigna_hum_rel, hum_rel_min, hum_rel_max ])
            con.commit()
            print("Guardado correctamente")
        except sqlite3.OperationalError as error:
	        print("Error al abrir:", error)
        finally:
            BD.sql_con_close(con)

    def UpdateActuador(clima):
        try:
            con = BD.sql_connection()
            sentencia = "UPDATE actuadores SET NOMBRE=?, CONSIGNA_TEMP=?, MAX_TEMP=?, MIN_TEMP=?, CONSIGNA_HUM_REL=?, HUM_REL_MIN=?, HUM_REAL_MAX=? WHERE ID=?"
            cursor = con.execute(sentencia, [clima.id, clima.nombre, clima.consigna_temp, clima.max_temp, clima.min_temp, consigna_hum_rel, hum_rel_min, hum_rel_max])
            con.commit()
            print("Actualizado correctamente")
        except sqlite3.OperationalError as error:
	        print("Error al abrir:", error)
        finally:
            BD.sql_con_close()

    def DeleteClima(clima):
        try:
            con = BD.sql_connection()
            sentencia = "DELETE FROM clima WHERE ID=?"
            cursor = con.execute(sentencia, clima.id)
            con.commit()
            print("Borrado correctamente")
        except sqlite3.OperationalError as error:
	        print("Error al abrir:", error)
        finally:
            BD.sql_con_close()

    def DeleteClima(id):
        try:
            con = BD.sql_connection()
            sentencia = "DELETE FROM clima WHERE ID=?"
            cursor = con.execute(sentencia, id)
            con.commit()
            print("Borrado correctamente")
        except sqlite3.OperationalError as error:
	        print("Error al abrir:", error)
        finally:
            BD.sql_con_close()

