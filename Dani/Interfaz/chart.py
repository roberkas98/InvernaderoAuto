
##__formateo_fecha__(f=[],opcion=4)
##
##
##clase "QGrafico"
##
##        Variables........................................................
##
##
##              chart {Guardará el gráfico listo para ser mostrado}
##              chart_view {Guardará un objeto QChartView con el gráfico
##                            actual que se está mostrando o se va  a mostrar
##                          }
##              lista {Guardará una lista con el siguiente formato
##                      [invernadero,unidad,fecha]
##              max {Guardará el valor máximo que se esperaba para la unidad de medida seleccionada}
##              min {Guardará el valor mínimo que se esperaba para la unidad de medida seleccionada}
##              serie_max {Guardará el valor máximo que debería tener la variable}
##              serie_min {Guardará el valor mínimo que debería tener la variable}
##              serie0 {QLineSeries() que guardará la lista de los datos de la gráfica}
##              serie1 {QLineSeries() que guardará la lista de los datos de la gráfica}
##              titulo {Guardará el título de la gráfica}
##
##
##
##
##        Métodos........................................................
##              _actualizar_(self,lista=[])????
##              _crear_gráfico_(lista=[])????
##              _crear_random_ {Crea una tabla random de datos para la gráfica}
##



import sys
from PySide6.QtCore import QPointF
from PySide6.QtGui import QPainter
from PySide6.QtWidgets import QMainWindow, QApplication
from PySide6.QtCharts import QChart, QChartView, QLineSeries
from datetime import datetime
import random
#FUNCIONES GENERALES DEL MODULO "CHART"

def __formateo_fecha__(f=[],opcion=4):
    año = f[0]
    mes = f[1]
    dia = f[2]
    minuto = f[3]
    segundo = f[4]
    
    if opcion == 1:
        return((año))
    if opcion == 2:
        return((año,mes))
    if opcion == 3:
        return((año,mes,dia))
    if opcion == 4:
        return((año,mes,dia,hora))
    if opcion == 5:
        return((año,mes,dia,hora,minuto))
    if opcion == 6:
        return((año,mes,dia,hora,minuto,segundo))
    else:
        print("Error de fecha")
        pass


#CLASES DEL MÓDULO QGrafico

class QGrafico():
    def __init__(self):
        super().__init__()


        ##VARIABLES
        self.color_max = ""
        self.chrt = None
        self.color_min = ""
        self.lista = ""
        self.max = 6
        self.min = 3
        self.series0 = None
        self.series1 = None
        self.titulo = "Titulo estándar"


        

        
        try:
            self._actualizar_(lista)
        except Exception as e:
            print("Error")
            print(e)
            self._crear_random_()

        finally:
            pass

        
    ##FUNCIONES

        
    def _actualizar_(self,lista=[]):
        
        self.titulo = lista[0]
        self.max = lista[1]
        self.min = lista[2]
        self.lista = lista
        self._crear_grafico_(self.lista)
        
    def _crear_grafico_(self,lista=[]):

        self.serie0
        

        
    def _crear_random_(self):
        self.series0 = QLineSeries()
        for i in range(24):
            self.series0.append(i,random.randint(self.min-4,self.max+4))

        self.series1 = QLineSeries()
        for i in range(24):
            self.series1.append(i,random.randint(self.min-4,self.max+4))


        self.serie_max = QLineSeries()
        self.serie_max.append(0,self.max)
        self.serie_max.append(24,self.max)

        self.serie_min = QLineSeries()
        self.serie_min.append(0,self.min)
        self.serie_min.append(24,self.min)
        
        self.chart = QChart()
        self.chart.legend().hide()
        self.chart.addSeries(self.series0)
        self.chart.addSeries(self.series1)
        self.chart.addSeries(self.serie_max)
        self.chart.addSeries(self.serie_min)

        self.chart.createDefaultAxes()
        self.chart.setTitle(self.titulo)

        self.chart_view = QChartView(self.chart)
        self.chart_view.setRenderHint(QPainter.Antialiasing)


        

if __name__ == "__main__":
    
    app = QApplication(sys.argv)

    window = QMainWindow()

    grafico = QGrafico()
    window.setCentralWidget(grafico.chart_view)
    window.show()
    window.resize(440, 300)
    sys.exit(app.exec())

