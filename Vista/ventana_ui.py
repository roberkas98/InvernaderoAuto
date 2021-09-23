# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'VAnadirInvernadero.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_VAnadirInvernadero(object):
    def setupUi(self, VAnadirInvernadero):
        VAnadirInvernadero.setObjectName("VAnadirInvernadero")
        VAnadirInvernadero.resize(800, 480)
        VAnadirInvernadero.setMinimumSize(QtCore.QSize(800, 480))
        VAnadirInvernadero.setMaximumSize(QtCore.QSize(800, 480))
        VAnadirInvernadero.setBaseSize(QtCore.QSize(800, 480))
        font = QtGui.QFont()
        font.setPointSize(12)
        VAnadirInvernadero.setFont(font)
        VAnadirInvernadero.setStyleSheet("/*Copyright (c) DevSec Studio. All rights reserved.\n"
"\n"
"MIT License\n"
"\n"
"Permission is hereby granted, free of charge, to any person obtaining a copy\n"
"of this software and associated documentation files (the \"Software\"), to deal\n"
"in the Software without restriction, including without limitation the rights\n"
"to use, copy, modify, merge, publish, distribute, sublicense, and/or sell\n"
"copies of the Software, and to permit persons to whom the Software is\n"
"furnished to do so, subject to the following conditions:\n"
"\n"
"The above copyright notice and this permission notice shall be included in all\n"
"copies or substantial portions of the Software.\n"
"\n"
"THE SOFTWARE IS PROVIDED *AS IS*, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR\n"
"IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,\n"
"FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE\n"
"AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER\n"
"LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,\n"
"OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.\n"
"*/\n"
"\n"
"/*-----QWidget-----*/\n"
"QWidget\n"
"{\n"
"    background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(27, 39, 50, 255),stop:1 rgba(47, 53, 74, 255));\n"
"    color: white;\n"
"    border-radius: 9px;\n"
"}\n"
"\n"
"\n"
"/*-----QLabel-----*/\n"
"QLabel\n"
"{\n"
"    background-color: transparent;\n"
"    color: #c2c7d5;\n"
"    font-size: 18px;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QPushButton-----*/\n"
"QPushButton\n"
"{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.511, x2:1, y2:0.511, stop:0 rgba(0, 172, 149, 255),stop:0.995192 rgba(54, 197, 177, 255));\n"
"    color: #fff;\n"
"    font-size: 15px;\n"
"    font-weight: bold;\n"
"    border: none;\n"
"    border-radius: 3px;\n"
"    padding: 10px;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.511, x2:1, y2:0.511, stop:0 rgba(0, 207, 179, 255),stop:1 rgba(70, 255, 230, 255));\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QCheckBox-----*/\n"
"QCheckBox\n"
"{\n"
"    background-color: transparent;\n"
"    color: #fff;\n"
"    font-size: 10px;\n"
"    font-weight: bold;\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QCheckBox-----*/\n"
"QCheckBox::indicator\n"
"{\n"
"    color: #b1b1b1;\n"
"    background-color: #323232;\n"
"    border: 1px solid darkgray;\n"
"    width: 12px;\n"
"    height: 12px;\n"
"\n"
"}\n"
"\n"
"\n"
"QCheckBox::indicator:checked\n"
"{\n"
"    image:url(\"./ressources/check.png\");\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.511, x2:1, y2:0.511, stop:0 rgba(0, 172, 149, 255),stop:0.995192 rgba(54, 197, 177, 255));;\n"
"    border: 1px solid #607cff;\n"
"\n"
"}\n"
"\n"
"\n"
"QCheckBox::indicator:unchecked:hover\n"
"{\n"
"    border: 1px solid #08b099;\n"
"\n"
"}\n"
"\n"
"\n"
"QCheckBox::disabled\n"
"{\n"
"    color: #656565;\n"
"\n"
"}\n"
"\n"
"\n"
"QCheckBox::indicator:disabled\n"
"{\n"
"    background-color: #656565;\n"
"    color: #656565;\n"
"    border: 1px solid #656565;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QLineEdit-----*/\n"
"QLineEdit\n"
"{\n"
"    background-color: #c2c7d5;\n"
"    color: #000;\n"
"    font-weight: bold;\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"    padding: 3px;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QListView-----*/\n"
"QListView\n"
"{\n"
"    background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(50, 61, 80, 255),stop:1 rgba(44, 49, 69, 255));\n"
"    color: #fff;\n"
"    font-size: 12px;\n"
"    font-weight: bold;\n"
"    border: 1px solid #191919;\n"
"    show-decoration-selected: 0;\n"
"\n"
"}\n"
"\n"
"\n"
"QListView::item\n"
"{\n"
"    color: #31cecb;\n"
"    background-color: #454e5e;\n"
"    border: none;\n"
"    padding: 5px;\n"
"    border-radius: 0px;\n"
"    padding-left : 10px;\n"
"    height: 42px;\n"
"\n"
"}\n"
"\n"
"QListView::item:selected\n"
"{\n"
"    color: #31cecb;\n"
"    background-color: #454e5e;\n"
"\n"
"}\n"
"\n"
"\n"
"QListView::item:!selected\n"
"{\n"
"    color:white;\n"
"    background-color: transparent;\n"
"    border: none;\n"
"    padding-left : 10px;\n"
"\n"
"}\n"
"\n"
"\n"
"QListView::item:!selected:hover\n"
"{\n"
"    color: #bbbcba;\n"
"    background-color: #454e5e;\n"
"    border: none;\n"
"    padding-left : 10px;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QTreeView-----*/\n"
"QTreeView \n"
"{\n"
"    background-color: #232939;\n"
"    show-decoration-selected: 0;\n"
"    color: #c2c8d7;\n"
"\n"
"}\n"
"\n"
"\n"
"QTreeView::item \n"
"{\n"
"    border-top-color: transparent;\n"
"    border-bottom-color: transparent;\n"
"\n"
"}\n"
"\n"
"\n"
"QTreeView::item:hover \n"
"{\n"
"    background-color: #606060;\n"
"    color: #fff;\n"
"\n"
"}\n"
"\n"
"\n"
"QTreeView::item:selected \n"
"{\n"
"    background-color: #0ab19a;\n"
"    color: #fff;\n"
"\n"
"}\n"
"\n"
"\n"
"QTreeView::item:selected:active\n"
"{\n"
"    background-color: #0ab19a;\n"
"    color: #fff;\n"
"\n"
"}\n"
"\n"
"\n"
"QTreeView::branch:has-children:!has-siblings:closed,\n"
"QTreeView::branch:closed:has-children:has-siblings \n"
"{\n"
"    image: url(://tree-closed.png);\n"
"\n"
"}\n"
"\n"
"QTreeView::branch:open:has-children:!has-siblings,\n"
"QTreeView::branch:open:has-children:has-siblings  \n"
"{\n"
"    image: url(://tree-open.png);\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QTableView & QTableWidget-----*/\n"
"QTableView\n"
"{\n"
"    background-color: #232939;\n"
"    border: 1px solid gray;\n"
"    color: #f0f0f0;\n"
"    gridline-color: #232939;\n"
"    outline : 0;\n"
"\n"
"}\n"
"\n"
"\n"
"QTableView::disabled\n"
"{\n"
"    background-color: #242526;\n"
"    border: 1px solid #32414B;\n"
"    color: #656565;\n"
"    gridline-color: #656565;\n"
"    outline : 0;\n"
"\n"
"}\n"
"\n"
"\n"
"QTableView::item:hover \n"
"{\n"
"    background-color: #606060;\n"
"    color: #f0f0f0;\n"
"\n"
"}\n"
"\n"
"\n"
"QTableView::item:selected \n"
"{\n"
"    background-color: #0ab19a;\n"
"    color: #F0F0F0;\n"
"\n"
"}\n"
"\n"
"\n"
"QTableView::item:selected:disabled\n"
"{\n"
"    background-color: #1a1b1c;\n"
"    border: 2px solid #525251;\n"
"    color: #656565;\n"
"\n"
"}\n"
"\n"
"\n"
"QTableCornerButton::section\n"
"{\n"
"    background-color: #343a49;\n"
"    color: #fff;\n"
"\n"
"}\n"
"\n"
"\n"
"QHeaderView::section\n"
"{\n"
"    color: #fff;\n"
"    border-top: 0px;\n"
"    border-bottom: 1px solid gray;\n"
"    border-right: 1px solid gray;\n"
"    background-color: #343a49;\n"
"    margin-top:1px;\n"
"    margin-bottom:1px;\n"
"    padding: 5px;\n"
"\n"
"}\n"
"\n"
"\n"
"QHeaderView::section:disabled\n"
"{\n"
"    background-color: #525251;\n"
"    color: #656565;\n"
"\n"
"}\n"
"\n"
"\n"
"QHeaderView::section:checked\n"
"{\n"
"    color: #fff;\n"
"    background-color: #0ab19a;\n"
"\n"
"}\n"
"\n"
"\n"
"QHeaderView::section:checked:disabled\n"
"{\n"
"    color: #656565;\n"
"    background-color: #525251;\n"
"\n"
"}\n"
"\n"
"\n"
"QHeaderView::section::vertical::first,\n"
"QHeaderView::section::vertical::only-one\n"
"{\n"
"    border-top: 1px solid #353635;\n"
"\n"
"}\n"
"\n"
"\n"
"QHeaderView::section::vertical\n"
"{\n"
"    border-top: 1px solid #353635;\n"
"\n"
"}\n"
"\n"
"\n"
"QHeaderView::section::horizontal::first,\n"
"QHeaderView::section::horizontal::only-one\n"
"{\n"
"    border-left: 1px solid #353635;\n"
"\n"
"}\n"
"\n"
"\n"
"QHeaderView::section::horizontal\n"
"{\n"
"    border-left: 1px solid #353635;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QScrollBar-----*/\n"
"QScrollBar:horizontal \n"
"{\n"
"    background-color: transparent;\n"
"    height: 8px;\n"
"    margin: 0px;\n"
"    padding: 0px;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::handle:horizontal \n"
"{\n"
"    border: none;\n"
"    min-width: 100px;\n"
"    background-color: #56576c;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-line:horizontal, \n"
"QScrollBar::sub-line:horizontal,\n"
"QScrollBar::add-page:horizontal, \n"
"QScrollBar::sub-page:horizontal \n"
"{\n"
"    width: 0px;\n"
"    background-color: transparent;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar:vertical \n"
"{\n"
"    background-color: transparent;\n"
"    width: 8px;\n"
"    margin: 0;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::handle:vertical \n"
"{\n"
"    border: none;\n"
"    min-height: 100px;\n"
"    background-color: #56576c;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-line:vertical, \n"
"QScrollBar::sub-line:vertical,\n"
"QScrollBar::add-page:vertical, \n"
"QScrollBar::sub-page:vertical \n"
"{\n"
"    height: 0px;\n"
"    background-color: transparent;\n"
"\n"
"}\n"
"\n"
"/*añadido mio*/\n"
"QGroupBox{\n"
"    background-color: #506874;\n"
"    border-radius: 1em;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"}\n"
"\n"
"QComboBox{\n"
"}\n"
"\n"
"\n"
"")
        VAnadirInvernadero.setModal(True)
        self.botones = QtWidgets.QDialogButtonBox(VAnadirInvernadero)
        self.botones.setGeometry(QtCore.QRect(280, 392, 176, 64))
        self.botones.setOrientation(QtCore.Qt.Horizontal)
        self.botones.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Save)
        self.botones.setCenterButtons(True)
        self.botones.setObjectName("botones")
        self.label = QtWidgets.QLabel(VAnadirInvernadero)
        self.label.setGeometry(QtCore.QRect(175, 7, 161, 51))
        self.label.setObjectName("label")
        self.id = QtWidgets.QLineEdit(VAnadirInvernadero)
        self.id.setGeometry(QtCore.QRect(343, 21, 191, 31))
        self.id.setObjectName("id")
        self.areasRiego = QtWidgets.QGroupBox(VAnadirInvernadero)
        self.areasRiego.setGeometry(QtCore.QRect(189, 98, 379, 288))
        self.areasRiego.setAutoFillBackground(False)
        self.areasRiego.setObjectName("areasRiego")
        self.consignaHumedadSuelo = QtWidgets.QSpinBox(self.areasRiego)
        self.consignaHumedadSuelo.setGeometry(QtCore.QRect(161, 63, 61, 31))
        self.consignaHumedadSuelo.setStyleSheet("")
        self.consignaHumedadSuelo.setMaximum(100)
        self.consignaHumedadSuelo.setSingleStep(5)
        self.consignaHumedadSuelo.setObjectName("consignaHumedadSuelo")
        self.label_4 = QtWidgets.QLabel(self.areasRiego)
        self.label_4.setGeometry(QtCore.QRect(13, 65, 155, 27))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.label_4.setFont(font)
        self.label_4.setTextFormat(QtCore.Qt.RichText)
        self.label_4.setObjectName("label_4")
        self.cbAreaRiego = QtWidgets.QComboBox(self.areasRiego)
        self.cbAreaRiego.setGeometry(QtCore.QRect(10, 30, 241, 22))
        self.cbAreaRiego.setStyleSheet("")
        self.cbAreaRiego.setObjectName("cbAreaRiego")
        self.cbSensorMaster = QtWidgets.QComboBox(self.areasRiego)
        self.cbSensorMaster.setGeometry(QtCore.QRect(140, 154, 232, 22))
        self.cbSensorMaster.setStyleSheet("")
        self.cbSensorMaster.setObjectName("cbSensorMaster")
        self.label_6 = QtWidgets.QLabel(self.areasRiego)
        self.label_6.setGeometry(QtCore.QRect(5, 155, 120, 21))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.cbSensorEsclavo = QtWidgets.QComboBox(self.areasRiego)
        self.cbSensorEsclavo.setGeometry(QtCore.QRect(140, 189, 232, 22))
        self.cbSensorEsclavo.setObjectName("cbSensorEsclavo")
        self.label_7 = QtWidgets.QLabel(self.areasRiego)
        self.label_7.setGeometry(QtCore.QRect(7, 189, 127, 21))
        self.label_7.setObjectName("label_7")
        self.cbActuadorRiego = QtWidgets.QComboBox(self.areasRiego)
        self.cbActuadorRiego.setGeometry(QtCore.QRect(140, 224, 232, 22))
        self.cbActuadorRiego.setObjectName("cbActuadorRiego")
        self.label_8 = QtWidgets.QLabel(self.areasRiego)
        self.label_8.setGeometry(QtCore.QRect(5, 217, 134, 31))
        self.label_8.setObjectName("label_8")
        self.actuadores = QtWidgets.QGroupBox(VAnadirInvernadero)
        self.actuadores.setGeometry(QtCore.QRect(572, 98, 218, 288))
        self.actuadores.setStyleSheet("")
        self.actuadores.setObjectName("actuadores")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.actuadores)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_10 = QtWidgets.QLabel(self.actuadores)
        self.label_10.setMaximumSize(QtCore.QSize(16777215, 60))
        self.label_10.setObjectName("label_10")
        self.verticalLayout_2.addWidget(self.label_10)
        self.cbActuadorVentilacion = QtWidgets.QComboBox(self.actuadores)
        self.cbActuadorVentilacion.setStyleSheet("")
        self.cbActuadorVentilacion.setObjectName("cbActuadorVentilacion")
        self.verticalLayout_2.addWidget(self.cbActuadorVentilacion)
        self.label_11 = QtWidgets.QLabel(self.actuadores)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_2.addWidget(self.label_11)
        self.cbActuadorEnfriar = QtWidgets.QComboBox(self.actuadores)
        self.cbActuadorEnfriar.setStyleSheet("")
        self.cbActuadorEnfriar.setObjectName("cbActuadorEnfriar")
        self.verticalLayout_2.addWidget(self.cbActuadorEnfriar)
        self.label_15 = QtWidgets.QLabel(self.actuadores)
        self.label_15.setObjectName("label_15")
        self.verticalLayout_2.addWidget(self.label_15)
        self.cbActuadorHumidificador = QtWidgets.QComboBox(self.actuadores)
        self.cbActuadorHumidificador.setObjectName("cbActuadorHumidificador")
        self.verticalLayout_2.addWidget(self.cbActuadorHumidificador)
        self.label_12 = QtWidgets.QLabel(self.actuadores)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_2.addWidget(self.label_12)
        self.cbActuadorCalefaccion = QtWidgets.QComboBox(self.actuadores)
        self.cbActuadorCalefaccion.setObjectName("cbActuadorCalefaccion")
        self.verticalLayout_2.addWidget(self.cbActuadorCalefaccion)
        self.consignas_2 = QtWidgets.QGroupBox(VAnadirInvernadero)
        self.consignas_2.setGeometry(QtCore.QRect(7, 98, 176, 288))
        self.consignas_2.setAutoFillBackground(False)
        self.consignas_2.setObjectName("consignas_2")
        self.label_14 = QtWidgets.QLabel(self.consignas_2)
        self.label_14.setGeometry(QtCore.QRect(13, 78, 143, 34))
        self.label_14.setObjectName("label_14")
        self.areaRiego = QtWidgets.QSpinBox(self.consignas_2)
        self.areaRiego.setGeometry(QtCore.QRect(13, 184, 143, 18))
        self.areaRiego.setMaximum(100)
        self.areaRiego.setSingleStep(5)
        self.areaRiego.setObjectName("areaRiego")
        self.label_13 = QtWidgets.QLabel(self.consignas_2)
        self.label_13.setGeometry(QtCore.QRect(13, 144, 143, 33))
        self.label_13.setObjectName("label_13")
        self.label_9 = QtWidgets.QLabel(self.consignas_2)
        self.label_9.setGeometry(QtCore.QRect(13, 13, 143, 33))
        self.label_9.setStyleSheet("")
        self.label_9.setObjectName("label_9")
        self.horizontalSlider = QtWidgets.QSlider(self.consignas_2)
        self.horizontalSlider.setGeometry(QtCore.QRect(7, 56, 160, 22))
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.horizontalSlider_2 = QtWidgets.QSlider(self.consignas_2)
        self.horizontalSlider_2.setGeometry(QtCore.QRect(7, 105, 160, 22))
        self.horizontalSlider_2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_2.setObjectName("horizontalSlider_2")

        self.retranslateUi(VAnadirInvernadero)
        self.botones.accepted.connect(VAnadirInvernadero.accept)
        self.botones.rejected.connect(VAnadirInvernadero.reject)
        QtCore.QMetaObject.connectSlotsByName(VAnadirInvernadero)

    def retranslateUi(self, VAnadirInvernadero):
        _translate = QtCore.QCoreApplication.translate
        VAnadirInvernadero.setWindowTitle(_translate("VAnadirInvernadero", "Dialog"))
        self.botones.setToolTip(_translate("VAnadirInvernadero", "<html><head/><body><p>Añadir</p></body></html>"))
        self.label.setText(_translate("VAnadirInvernadero", "<html><head/><body><p><span style=\" font-size:14pt;\">ID Invernadero:</span></p></body></html>"))
        self.areasRiego.setTitle(_translate("VAnadirInvernadero", "Areas Riego"))
        self.label_4.setText(_translate("VAnadirInvernadero", "<html><head/><body><p><span style=\" font-size:12pt;\">Humedad suelo:</span></p></body></html>"))
        self.label_6.setText(_translate("VAnadirInvernadero", "<html><head/><body><p>Sensor master:</p></body></html>"))
        self.label_7.setText(_translate("VAnadirInvernadero", "<html><head/><body><p>Sensor esclavo:</p></body></html>"))
        self.label_8.setText(_translate("VAnadirInvernadero", "<html><head/><body><p>Actuador riego:</p></body></html>"))
        self.actuadores.setTitle(_translate("VAnadirInvernadero", "Actuadores"))
        self.label_10.setText(_translate("VAnadirInvernadero", "<html><head/><body><p>Ventilacion:</p></body></html>"))
        self.label_11.setText(_translate("VAnadirInvernadero", "<html><head/><body><p>Actuador enfriar:</p></body></html>"))
        self.label_15.setText(_translate("VAnadirInvernadero", "<html><head/><body><p>Humidificador:</p></body></html>"))
        self.label_12.setText(_translate("VAnadirInvernadero", "<html><head/><body><p>Calefaccion:</p></body></html>"))
        self.consignas_2.setTitle(_translate("VAnadirInvernadero", "Consignas"))
        self.label_14.setText(_translate("VAnadirInvernadero", "<html><head/><body><p>Humedad:</p></body></html>"))
        self.label_13.setText(_translate("VAnadirInvernadero", "<html><head/><body><p>Areas de Riego:</p></body></html>"))
        self.label_9.setToolTip(_translate("VAnadirInvernadero", "<html><head/><body><p><br/></p></body></html>"))
        self.label_9.setText(_translate("VAnadirInvernadero", "<html><head/><body><p>Temperatura:</p></body></html>"))

import resources_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    VAnadirInvernadero = QtWidgets.QDialog()
    ui = Ui_VAnadirInvernadero()
    ui.setupUi(VAnadirInvernadero)
    VAnadirInvernadero.show()
    sys.exit(app.exec_())

