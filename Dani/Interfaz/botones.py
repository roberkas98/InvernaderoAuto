#Aquí se encuentran todas las funciones de los botones

casimiro="2"

def b_atras(pantalla):
    if pantalla.ui_nom_ant == pantalla.ui_nom:
        return
    pantalla.AtrasUi()
    pantalla.CargarUi(pantalla.ui_nom_ant)
    pantalla.ActualizarQss()


def b_datalog(pantalla):
    pantalla.CargarUi("data_log")



def CargarUi(nombre):
    programa.ui.hide()
    
    programa.ui.ui_nom_ant = ui.ui_nom
    ui_nom = nombre

    q_ventana = QFile(dic[nombre]["ui"])
    if not q_ventana.open(QIODevice.ReadOnly):
        print(f"Imposible abrir {ventana}:{q_ventana.errorString()}")
        sys.exit(-1)
    cargador = QUiLoader()
    ui = cargador.load(q_ventana)
    q_ventana.close()
    if not self.ui:
        print(loader.errorString())
        sys.exit(-1)



    if nombre == "data_log":
        self.ui.boton_atras.clicked.connect(lambda: self.botones("butatras"))


    elif nombre == "menu":
        self.ui.buthum.clicked.connect(lambda: self.botones("buttdatalog"))
        self.ui.buttem.clicked.connect(lambda: _b_tem_())
        self.ui.buttdatalog.clicked.connect(lambda: self.botones("buttdatalog"))

    else:
        print("Error en el ui")
    return ui

##
##
##def b_buthum(pantalla):
##
##
##
##def b_buttemp(pantalla):
##
##
##
##
##def b_butgen(pantalla):
