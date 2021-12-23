    ##
##menu (ventana)
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




class menu(QWidget):
    def __init__(self):
        self = CargarUi()

        

##    crear la ui
##    editar la ui
##        crear el grafico
##        cargar el grafico
##    asociar los botones
##    mostrar la ui



    def _cargar_menu_(self):
        pass

    def _cargar_grafica_(self):
        self.Layout_2.addWidget(self.grafico.chart_view)
    def _actualizar_pantalla_(self):
        pass

    def _cambiar_titulo_(self,titulo):
        self.titulo_grafica = titulo
        pass
