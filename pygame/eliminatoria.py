from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QFont, QPen
from PyQt5.QtCore import QPointF
from PyQt5.QtWidgets import QGraphicsTextItem
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor, QPen
from controler import Controler
from partido import Partido
from PyQt5 import QtGui
from jugador import Jugador
from PyQt5.QtWidgets import QComboBox
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QApplication, QInputDialog


class Eliminatoria: 

    def __init__(self):
        # ... código anterior ...
        
        self.horizontal = False  # Variable de estado para determinar la orientación del árbol
        self.raiz_resultado = None
        self.cont = 0
        self.goles_totales = 0 
        
    def eliminatorias(self,tournament):
        app = QtWidgets.QApplication([])
        partido = Partido()
        jugador = Jugador()
        scene = QtWidgets.QGraphicsScene()  # Create a new scene
        global lista
        lista = tournament.clasificados_grupo()
        listasegundos =  jugador.sacar_segundos(lista)

        window = QtWidgets.QMainWindow()
        window.setWindowTitle("Fase de Octavos de Final")
        widget = QtWidgets.QWidget()  # Create a new widget
        nueva_permu = QtWidgets.QPushButton('Juguar una nueva permutacion', widget)
        nueva_permu.move(1200, 900)  # Mueve el botón a la posición (50, 50) en el widget
        nueva_permu.clicked.connect(lambda: self.jugar_permutaciones(tournament,scene,lista,partido))


        label_title = QtWidgets.QLabel("ELIMINATORIAS", widget)
        label_title.setFont(QFont('Verdana', 25))  # Set font and size
        label_title.setGeometry(820, 50, 500, 50)  # Set the position and size of the label


        label_mayor_salario=QtWidgets.QLabel(str(jugador.segundos_salario(listasegundos)),widget)
        label_mayor_salario.setFont(QFont('Verdana', 10))  # Set font and size
        label_mayor_salario.move(400,850)

        label_mayorAl=QtWidgets.QLabel(str(jugador.mayor_altura(lista)),widget)
        label_mayorAl.setFont(QFont('Verdana', 10))  # Set font and size
        label_mayorAl.move(400,900)

        label_menoral=QtWidgets.QLabel(str(jugador.menor_altura(lista)),widget)
        label_menoral.setFont(QFont('Verdana', 10))  # Set font and size
        label_menoral.move(400,950) 

        cambiar_orientacion = QtWidgets.QPushButton('Cambiar orientación', widget)
        cambiar_orientacion.move(1200, 800)  # Mueve el botón a la posición (1150, 800) en el widget
        cambiar_orientacion.clicked.connect(lambda: self.cambiar_orientacion(scene,partido))  # Conectar el botón a la 

        view = QtWidgets.QGraphicsView(scene, widget)  # Create a view for the scene
        view.setGeometry(350, 200, 1500, 500)  # Set the position and size of the view

        window.setCentralWidget(widget)


        grupos = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
        for i, grupo in enumerate(grupos):
            
            grupo_box = QtWidgets.QGroupBox(widget)  # Create a group box for each group
            grupo_box.setStyleSheet("QGroupBox { border: 2px solid black; border-radius: 10px; }")  # Set style
            grupo_box.setFixedWidth(200)  # Set fixed width
            grupo_box.setGeometry(50, 100+ i * 120, 250, 90)  # Set the geometry of the group box

            grupo_label = QtWidgets.QLabel(f"Grupo {grupo}", grupo_box)
            grupo_label.setFont(QFont('Verdana', 12))
            grupo_label.move(50, 10)  # Move the group label within the group box

            equipo1_label = QtWidgets.QLabel(lista[i].get_name() + " " + str(lista[i].get_ganaPor2()) , grupo_box)
            equipo1_label.setFont(QFont('Verdana', 8))
            equipo1_label.move(50, 40)  # Move the team 1 label within the group box

            equipo2_label = QtWidgets.QLabel(lista[i+1].get_name() + " " + str(lista[i+1].get_ganaPor2()), grupo_box)
            equipo2_label.setFont(QFont('Verdana', 8))
            equipo2_label.move(50, 70)  # Move the team 2 label within the group box
        
        
        

        window.show()  # Show the window
        app.exec_()
    

    def raiz_resultado(self, tournament, lista):
        primera_mitad = lista[:8]
        segunda_mitad = lista[8:]
        controler = Controler()
        permu = tournament.permutaciones_arbol(primera_mitad,segunda_mitad,self.cont)            
        self.raiz_resultado = controler.jugar_permutacion(permu)
        return self.raiz_resultado

    def cambiar_orientacion(self,scene,partido):
        self.horizontal = not self.horizontal
        if not self.horizontal:
            # Actualiza la interfaz de usuario para mostrar la nueva permutación
            self.goles_totales = partido.goles_totales
            scene.clear()
            label_goles = QtWidgets.QLabel("Goles totales de la segunda fase: " + str(self.goles_totales))
            label_goles.setFont(QFont('Verdana', 5))  # Set font and size
            proxy = QtWidgets.QGraphicsProxyWidget()
            proxy.setWidget(label_goles)
            scene.addItem(proxy)
            proxy.setPos(100, 300)  # Mueve el QLabel a la posición (400, 800) en la escena
            tree_drawer = TreeDrawer(scene)
            tree_drawer.draw_node(self.raiz_resultado, 700, 50, 370)
            
        else:
            # Actualiza la interfaz de usuario para mostrar la nueva permutación
            self.goles_totales = partido.goles_totales
            scene.clear()
            label_goles = QtWidgets.QLabel("Goles totales de la segunda fase: " + str(self.goles_totales))
            label_goles.setFont(QFont('Verdana', 5))  # Set font and size
            proxy = QtWidgets.QGraphicsProxyWidget()
            proxy.setWidget(label_goles)
            scene.addItem(proxy)
            proxy.setPos(100, 300)  # Mueve el QLabel a la posición (400, 800) en la escena
            tree_drawer = TreeDrawer(scene)
            tree_drawer.draw_node_horizontal(self.raiz_resultado, 100, 50, 170, 100)

    def jugar_permutaciones(self,tournament,scene,lista,partido): #MEJORAR
        print('hola')
        controler = Controler()
        primera_mitad = lista[:8]
        segunda_mitad = lista[8:]
        partido = Partido()
        permu = tournament.permutaciones_arbol(primera_mitad,segunda_mitad,self.cont)
                 
        self.raiz_resultado = controler.jugar_permutacion(permu)
        self.goles_totales = partido.goles_totales
        partido.goles_totales = 0   
        scene.clear()
        
        label_goles = QtWidgets.QLabel("Goles totales de la segunda fase: " + str(self.goles_totales))
        label_goles.setFont(QFont('Verdana', 5))  # Set font and size
        proxy = QtWidgets.QGraphicsProxyWidget()
        proxy.setWidget(label_goles)
        scene.addItem(proxy)
        proxy.setPos(100, 300)  # Mueve el QLabel a la posición (400, 800) en la escena
        nombres,dinero = controler.crear_diagrama(permu)
        tree_drawer = TreeDrawer(scene)
        if not self.horizontal:
            self.cont += 1  # Incrementa cont
            tree_drawer.draw_node(self.raiz_resultado, 700, 50, 370)
            # print("cual de los siguientes equipo desea quese muestre la ruta")
            # for c in lista:
            #     print (c.get_name())
            # equipo, ok = QInputDialog.getText(None, 'Input Dialog', 'Introduce el nombre del equipo:')
            # if ok:
            #     print("el equipo es " + equipo)
            #     self.amarillo(self.raiz_resultado,equipo)
        else:
            self.cont += 1  # Incrementa cont
            tree_drawer.draw_node_horizontal(self.raiz_resultado, 100, 50, 170, 100)
        tree_drawer.grafica_barras(nombres,dinero)
        # tree_drawer.draw_node_yellow(self.raiz_resultado, 100, 50, 170,"Brasil")
        
        

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root):
        self.root = Node(root)

class TreeDrawer:
    def __init__(self, scene):
        self.scene = scene
        self.pen = QPen(QColor("black"))
        self.font = QFont("Verdana", 5)  # Set the font and size
    

    def draw_node(self, node, x, y, distance):
        if node is not None:
            # self.scene.addRect(x, y, 120, 30, self.pen)
            
            text_item = self.scene.addText(str(node.get_info()), self.font)  # Set the font of the text
            text_item.setPos(x-30, y+2)
            self.scene.addItem(text_item)
            self.scene.addItem(text_item)
            if node.get_izq() is not None:
                self.scene.addLine(x + 25, y + 20, x - distance + 15, y + 40, self.pen)
                self.draw_node(node.get_izq(), x - distance, y + 40, distance / 2)
            if node.get_der() is not None:
                self.scene.addLine(x + 25, y + 20, x + distance + 35, y + 40, self.pen)
                self.draw_node(node.get_der(), x + distance, y + 40, distance / 2)

    def draw_node_horizontal(self, node, x, y, distance, x_offset=0):
        x += x_offset  # Añade el desplazamiento a x
        if node is not None:
            text_item = self.scene.addText(str(node.get_info()), self.font)
            text_item.setPos(x-80, y+20)
            self.scene.addItem(text_item)
            if node.get_izq() is not None:
                self.scene.addLine(x + 50, y + 25, x + 120, y - distance + 35, self.pen)
                self.draw_node_horizontal(node.get_izq(), x + 200, y - distance, distance / 2)
            if node.get_der() is not None:
                self.scene.addLine(x + 50, y + 25, x + 120, y + distance + 35, self.pen)
                self.draw_node_horizontal(node.get_der(), x + 200, y + distance, distance / 2)
    
    def grafica_barras(self,nombres, valores):
        plt.bar(nombres, valores)
        plt.xlabel('Nombres')
        plt.ylabel('Valores')
        plt.title('Gráfica de Barras')
        plt.show()
    
    # def draw_node_yellow(self, node, x, y, distance, string_parametro):
    #     if node is not None:
    #         text = str(node.get_info())
    #         lista1 = text.split()
    #         text_item = self.scene.addText(text, self.font)  # Agregar texto con la información del nodo
    #         text_item.setPos(x-30, y+2)
            
    #         if string_parametro == lista1[0] or string_parametro == lista1[3]:
    #             self.pen.setColor(Qt.yellow)  # Cambiar color de la línea a amarillo si coincide con el parámetro
                
    #         self.scene.addItem(text_item)
            
    #         if node.get_izq() is not None:
    #             self.scene.addLine(x + 25, y + 20, x - distance + 15, y + 120, self.pen)
    #             self.draw_node_yellow(node.get_izq(), x - distance, y + 120, distance / 2, string_parametro)
            
    #         if node.get_der() is not None:
    #             self.scene.addLine(x + 25, y + 20, x + distance + 35, y + 120, self.pen)
    #             self.draw_node_yellow(node.get_der(), x + distance, y + 120, distance / 2, string_parametro)

    # def amarillo(self,raiz,equipo):
    #     print("si llegue")
    #     amarillo = "\033[93m"
    #     fin_color = "\033[0m"
    #     eq=raiz.get_info()
    #     list=eq.split()
    #     if list[0]==equipo or list[3] ==equipo :
    #         print(raiz.get_info(),end="")
    #         print(amarillo+ "----------"+ fin_color)

    #         amarillo(raiz.get_der(),equipo)
    #         amarillo(raiz.get_izq(),equipo)
    #     else:
    #         amarillo(raiz.get_der(),equipo)
    #         amarillo(raiz.get_izq(),equipo)


