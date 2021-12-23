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






#Son los botones de la ventana "menu"

def b_datalog():

    #Acciones previas a realizar antes de esconder la ventana actual y mostrar la seleccionada

    CargarUi("data_log")

    #Acciones posteriores a enseñar en la página siguiente

def b_gen():

    #Acciones previas a realizar antes de esconder la ventana actual y mostrar la seleccionada

    #CargarGr([unidad],)
    pass
    #Acciones posteriores a enseñar en la página siguiente

def b_hum():

    #Acciones previas a realizar antes de esconder la ventana actual y mostrar la seleccionada

    pass
    #Acciones posteriores a enseñar en la página siguiente

def b_tem():

    #Acciones previas a realizar antes de esconder la ventana actual y mostrar la seleccionada

    pass
    #Acciones posteriores a enseñar en la página siguiente
