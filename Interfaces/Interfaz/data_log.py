"""
Esta es la pantalla data log
Es un objeto de la clase QWidget



Se le añaden las siguientes variables y métodos:

Variables:



"""
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from botones import CargarUi


class data_log(QWidget):

    def __init__(self) -> None:
        super().__init__()

        self.name="data_log"

        self = CargarUi(self.name)

    pass