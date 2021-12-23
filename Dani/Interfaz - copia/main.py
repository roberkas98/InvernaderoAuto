

import sys
from PySide6.QtUiTools import *
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6 import QtGui, QtCore

from py.botones import *
from py.chart import *
from py.data_log import *
from py.menu import *
from py.programa import *
from py.funciones import *



while True:
    
    app = QApplication(sys.argv)#Abrimos la app
    
    programa = QPrograma()#Iniciamos nuestra interfaz del programa

    programa.ui.show()#Mostramos la interfaz del programa

   

    programa.ui.setFixedSize(800,480)
    programa.ui.setWindowIcon(QtGui.QIcon("iconos/icono_granja.png"))
    programa.ui.setWindowTitle("Rober & Dani Company Registered")
 



    sys.exit(app.exec())
