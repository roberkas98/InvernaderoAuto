import sqlite3
from sqlite3 import Error





class BD:

    @staticmethod
    def sql_connection():

        try:
            con = sqlite3.connect('BD.db')
            print("Connection is established: Database is created in memory")
            return con

        except Error:
            print(Error)


    @staticmethod
    def sql_con_close(con):
        try:
            con.close()
        except Error:
            print(Error)

