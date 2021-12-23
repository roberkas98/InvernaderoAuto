#    Funciones de python

import sys
from PySide6.QtUiTools import *
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6 import QtGui, QtCore


def CargarUi(nombre="menu"):

    dic = {

    "menu":{"ui":"ui/menu_oscuro.ui"},
    "ajustes_generales":{"ui":"ui/ajustes_generales.ui"},
    "data_log":{"ui":"ui/data_log.ui"},
    "filtros_data_log":{"ui":"ui/filtros_data_log.ui"}

    }
    try:
        qui = QFile(dic[nombre]["ui"])

        ui = QUiLoader()
        ui = ui.load(qui)
        qui.close()
        return ui
    except Exception as e:
        print(e)
    finally:
        pass

def CargarGr(nombre):

    try:
        pass
    except Exception as e:
        print(e)
    finally:
        pass

