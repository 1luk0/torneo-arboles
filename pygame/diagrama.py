import sys
import numpy as np
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

class BarChart(QMainWindow):
    def __init__(self,lab,val):
        super().__init__()

        self.setWindowTitle("Desempeño equipos")
        self.setGeometry(100, 100, 800, 600)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        
        self.layout = QVBoxLayout(self.central_widget)

        # Creamos un lienzo de matplotlib
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.layout.addWidget(self.canvas)

        # Datos
        labels = lab
        values = val

        # Creamos el gráfico de barras
        self.ax = self.figure.add_subplot(111)
        self.ax.bar(labels, values)

        # Actualizamos el gráfico
        self.canvas.draw()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = BarChart()
    window.show()
    sys.exit(app.exec_())
