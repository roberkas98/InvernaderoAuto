
"""
app(QApplication)

    window(QMainWindow)

        [setCentralWidget]pantalla(Pantalla())(QWidget)

            "menu"
            "data_log"
            "filtros_data_log"


"""







import sys
from PySide6.QtUiTools import *
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6 import QtGui, QtCore

from chart import *

################################################################################################################        
################################################################################################################
################################################################################################################
################################################################################################################

class Pantalla(QWidget):


    def __init__(self):
        pantalla_inicial="menu"
        QWidget.__init__(self)

        self.ui_nom_ant=pantalla_inicial#Guardará siempre el nombre la pantalla en la que estemos o en la anterior en la que hayamos estado
        self.ui_nom = pantalla_inicial#Guardará siempre el nombre de la pantalla en la que estemos o a la que queramos ir
        self.ui = QWidget()#Inicializamos en un QWidget genérico
        self.ui0 = QWidget()
        self.qss =  "qss/"+pantalla_inicial+".qss"#Contendrá el directorio de la hoja de estilos qss actual o la que se quiera utilizar
        
        self.dic = {

        "menu":{"ui":"ui/menu_oscuro.ui","qss":"qss/menu.qss"},
        "ajustes_generales":{"ui":"ui/ajustes_generales.ui","qss":"qss/ajustes_generales.qss"},
        "data_log":{"ui":"ui/data_log.ui","qss":"qss/data_log_2.qss"},
        "filtros_data_log":{"ui":"ui/filtros_data_log.ui","qss":"qss/filtros_data_log.qss"}

        }
        #Este diccionario asocia a cada una de las pantallas con sus respestivas hojas ui y de estilo
        
        self.CargarUi(self.ui_nom)#Cargamos el Ui actual
        self.ActualizarQss()#Actualizamos el qss a utilizar

    def CargarUi(self,nombre):
        self.ui.hide()
        self.ui_nom_ant = self.ui_nom
        self.ui_nom = nombre

        q_ventana = QFile(self.dic[nombre]["ui"])
        if not q_ventana.open(QIODevice.ReadOnly):
            print(f"Imposible abrir {ventana}:{q_ventana.errorString()}")
            sys.exit(-1)
        cargador = QUiLoader()
        self.ui = cargador.load(q_ventana)
        q_ventana.close()
        if not self.ui:
            print(loader.errorString())
            sys.exit(-1)
        
        if nombre == "data_log":
            self.ui.boton_atras.clicked.connect(lambda: self.botones("butatras"))
        elif nombre == "menu":
            self.ui.buttdatalog.clicked.connect(lambda: self.botones("buttdatalog"))
            grafico = QGrafico()
            self.ui.Layout_2.addWidget(grafico.chart_view)
        #Aquí podemos añadir modificaciónes que formatearan a todas las pantallas
        self.ui.setWindowIcon(QtGui.QIcon("iconos/icono_granja.png"))
        self.ui.setWindowTitle("Rober & Dani Company Registered")
        
        self.ui.show()
        
    def ActualizarQss(self):
        try:
            n = self.dic[self.ui_nom]["qss"]
            file = QtCore.QFile(n)
            file.open(QtCore.QFile.ReadOnly | QtCore.QFile.Text)
            qss = QtCore.QTextStream(file)
            self.qss = qss
        except Exception as e:
            print(e)

            
    def AtrasUi(self):
        comodin=self.ui_nom_ant
        self.ui_nom_ant = self.ui_nom
        self.ui_nom = comodin



    def ActualizarPantalla(self):
        pass

    def botones(self,opcion):
        if opcion == "buttdatalog":
            #self.cambiar_menu()
            self.CargarUi("data_log")
        if opcion == "butatras":
            self.CargarUi("menu")#Enrealidad debería cambiar a la verdadera pantalla anterior
                    


################################################################################################################        
################################################################################################################
################################################################################################################        
################################################################################################################
################################################################################################################        
################################################################################################################
while True:
    app=QApplication(sys.argv)#Abrimos la app
    
    pantalla = Pantalla()#Iniciamos nuestra interfaz del programa

##    File = QtCore.QFile(pantalla.dic[pantalla.ui_nom]["qss"])
##    if not File.open( QtCore.QFile.ReadOnly | QtCore.QFile.Text):
##        break                                                                                                                                    
##
##    qss = QtCore.QTextStream(File)

    #Aplicamos el estilo de la página
    #app.setStyleSheet(qss.readAll())

    
    pantalla.ui.show()


##    pantalla.ui.se
   

    #pantalla.ui.setFixedSize(800,480)

 
##   pantalla.ui.buttdatalog.clicked.connect(pantalla.printear())

##    pantalla.ui.buttdatalog.clicked.connect(b.b_datalog())


    sys.exit(app.exec())
