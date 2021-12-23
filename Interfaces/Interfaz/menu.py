##
##menu
##    variables:
##        titulo_grafica{}
##
##    metodos:
##        _actualizar_pantalla_(){}
##        _cambiar_titulo_(){}
##
##








import sys
from PySide6.QtUiTools import *
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6 import QtGui, QtCore

import py.botones as b
import py.chart as c


class menu(QWidget):
    def __init__(self):
        super.__init__()

        self.titulo_grafica=""
        self.grafico = QGrafico()
        

    def __grafico_(self):
        pass
    def _actualizar_pantalla_(self):
        pass

    def cambiar_titulo(self,titulo):
        self.titulo_grafica = titulo
        
self.menuRegistro.aboutToShow.connect(lambda : self.stacked.setCurrentIndex(2))