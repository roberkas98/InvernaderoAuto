import sqlite3

from sqlite3 import Error

class BD:
    con = sqlite3
    def sql_connection():

        try:
            con = sqlite3.connect('BD.db')
            print("Connection is established: Database is created in memory")
            return con

        except Error:
            print(Error)

        finally:
            con.close()


    def sql_con_close():
        try:
            con.close
        except Error:
            print(Error)

