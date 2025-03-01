import pygame
import tkinter as tk
from tkinter import filedialog
import shutil
import os
from teams import Teams
from tournament import Tournament
from partido import Partido
from eliminatoria import Eliminatoria

pygame.init()
#pygame.mixer.init()
pygame.display.set_caption('Mundial Brazil 2014')
# Configuración de la pantalla
screen = pygame.display.set_mode((1250, 650))

alert_box = None
alert_timer = 0
#pygame.mixer.music.load('resources/y2mate.com - Sergio Mendes  Magalenha Official Visualizer.mp3')  # Reemplaza esto con la ruta a tu archivo de música
#pygame.mixer.music.play(-1)  # El argumento -1 hace que la música se repita indefinidamente
#--------------------CONFIGURACION DE TABLA-------------------------------
cell_width = 90
cell_height = 30
margin = 10
cols = 8
rows = 5
data = [[0] * 8 for _ in range(5)]
grid = [[pygame.Rect((cell_width + margin) * j, (cell_height + margin) * i, cell_width, cell_height) for j in range(cols)] for i in range(rows)]
white = (255, 255, 255)
black = (0, 0, 0)
group_text = pygame.font.Font(None, 25).render("Grupos", True, (0, 0, 0))
simular_f = [False,False,False]
simular_f1 = 0
simularf2 = 0

#--------------------FUENTES----------------------------------------------

fuente = pygame.font.Font(None, 24)
font_size = 22  # Cambia esto al tamaño de fuente que quieras
precisionF = pygame.font.Font(None, font_size)
groupF = pygame.font.Font(None,font_size)
color_inactive = pygame.Color('lightskyblue3')
color_active = pygame.Color('dodgerblue2')
color = color_inactive
active = False
font = pygame.font.Font(None, 25)
active_box = None
done = False

#--------------------------INPUTS-----------------------------------------------

# Configuración del input para "Nombre del equipo"
input_box1 = pygame.Rect(200, 25, 150, 20)
text1 = ''
input_text1 = pygame.font.Font(None, 22).render("Nombre del equipo ", True, (0, 0, 0))

# Configuración del input para "Resistencia"
input_box2 = pygame.Rect(200, 50, 150, 20)
text2 = ''
input_text2 = pygame.font.Font(None, 22).render("Resistencia ", True, (0, 0, 0))

# Configuración del input para "Fuerza"
input_box3 = pygame.Rect(200, 75, 150, 20)
text3 = ''
input_text3 = pygame.font.Font(None, 22).render("Fuerza ", True, (0, 0, 0))

# Configuración del input para "Velocidad"
input_box4 = pygame.Rect(200, 100, 150, 20)
text4 = ''
input_text4 = pygame.font.Font(None, 22).render("Velocidad ", True, (0, 0, 0))

input_box5 = pygame.Rect(800, 600, 150, 20)
text5 = ''
input_text5 = pygame.font.Font(None, 22).render("Descalificar equipo ", True, (0, 0, 0))

#--------------------MENUS DESPLEGABLES----------------------------------------

#Configuración del menú "Criterio"
menu_rect = pygame.Rect(470, 25, 150, 20)
menu_options = ["resistencia", "fuerza", "velocidad","precision"]
menu_active = False
selected_option = None

#Configuración del menú "Grupos"
groups = pygame.Rect(200, 250, 150, 20)
group_options = ["Grupo A", "Grupo B", "Grupo C", "Grupo D", "Grupo E", "Grupo F", "Grupo G", "Grupo H"]
group_active = False
groupO = None

#Configuración del menú "Costumbre de campo"
cost_rect = pygame.Rect(200, 125, 150, 20)
cost_options = ["Alto", "Medio", "Bajo"]
cost_active = False
cost_selected = None

#Configuración del menú "Presición"
pres_rect = pygame.Rect(200, 520, 150, 20)
pres_options = ["Alto", "Medio", "Bajo"]
pres_active = False
pres_selected = None

#Configuración del menú "Estadio"
sta_rect = pygame.Rect(750, 25, 150, 20)
sta_options = ["Alto", "Medio", "Bajo"]
sta_active = False
sta_selected = None

#--------------------BOTONES-----------------------------------------------

# Configuración del botón "Subir archivos"
subir_archivo = pygame.Rect(1000, 200, 140, 20)
border_width = 2
border = pygame.Rect(subir_archivo.left - border_width, subir_archivo.top - border_width, subir_archivo.width + 2*border_width, subir_archivo.height + 2*border_width)  # Rectángulo del borde
font = pygame.font.Font(None, 25)

# Configuración del botón "Ingresar"
ingresar = pygame.Rect(1050, 600, 140, 20)
border_ingresar = pygame.Rect(ingresar.left - border_width, ingresar.top - border_width, ingresar.width + 2*border_width, ingresar.height + 2*border_width)

ingresar_bandera = pygame.Rect(995, 160, 150, 20)
border_ingresar_bandera = pygame.Rect(ingresar_bandera.left - border_width, ingresar_bandera.top - border_width, ingresar_bandera.width + 2*border_width, ingresar_bandera.height + 2*border_width)

#Configuracion del botón "Simular Fecha"
simular = pygame.Rect(1075, 25, 140, 20)
boton_simular = pygame.Rect(simular.left - border_width, simular.top - border_width, simular.width + 2*border_width, simular.height + 2*border_width)

#--------------------BOTONES DE LA TABLA------------------------------------

A = pygame.Rect(500, 200, 50, 20)
boton_A = pygame.Rect(A.left - border_width, A.top - border_width, A.width + 2*border_width, A.height + 2*border_width)

B = pygame.Rect(550, 200, 50, 20)
boton_B = pygame.Rect(B.left - border_width, B.top - border_width, B.width + 2*border_width, B.height + 2*border_width)

C = pygame.Rect(600, 200, 50, 20)
boton_C = pygame.Rect(C.left - border_width, C.top - border_width, C.width + 2*border_width, C.height + 2*border_width)

D = pygame.Rect(650, 200, 50, 20)
boton_D = pygame.Rect(D.left - border_width, D.top - border_width, D.width + 2*border_width, D.height + 2*border_width)

E = pygame.Rect(700, 200, 50, 20)
boton_E = pygame.Rect(E.left - border_width, E.top - border_width, E.width + 2*border_width, E.height + 2*border_width)

F = pygame.Rect(750, 200, 50, 20)
boton_F = pygame.Rect(F.left - border_width, F.top - border_width, F.width + 2*border_width, F.height + 2*border_width)

G = pygame.Rect(800, 200,50, 20)
boton_G = pygame.Rect(G.left - border_width, G.top - border_width, G.width + 2*border_width, G.height + 2*border_width)

H = pygame.Rect(850, 200, 50, 20)
boton_H = pygame.Rect(H.left - border_width, H.top - border_width, H.width + 2*border_width, H.height + 2*border_width)

# Configuración de tkinter
root = tk.Tk()
root.withdraw()

bandera = 'resources/banderas/brazil.jpeg'

#-----------------------FUNCIONES-----------------------------------------

# Crear una matriz de 5x8 para almacenar los datos de los equipos
matriz = [['' for _ in range(8)] for _ in range(5)]

banderas = ['' for _ in range(5)]
cont_banderas = 0

# Dibujar la tabla
def draw_table(data):
    rows = len(data)
    cols = len(data[0])
    for i in range(rows):
        for j in range(cols):
            if i >= len(grid) or j >= len(grid[0]):
                pygame.display.set_caption('Los grupos no pueden contener más de 4 equipos')
            else:
                cell = grid[i][j]
                cell.x = j * cell.width + 450
                cell.y = i * cell.height + 230
                if j == 0:  # Solo cargar y dibujar la imagen cuando j es 1
                    nombre_equipo = data[i][j]
                    equipo = tournament.get_equipo(nombre_equipo)  # Buscar el objeto del equipo por nombre
                    if equipo and equipo.get_bandera():  # Comprobar si el equipo existe y tiene una bandera
                        bandera_img = pygame.image.load(equipo.get_bandera())
                        bandera_img = pygame.transform.scale(bandera_img, (40, 30))
                        screen.blit(bandera_img, (cell.x - 50, cell.y))
    for i in range(rows):
        for j in range(cols):
            if i >= len(grid) or j >= len(grid[0]):
                pygame.display.set_caption('Los grupos no pueden contener más de 4 equipos')
            else:
                cell = grid[i][j]
                pygame.draw.rect(screen, black, cell, 1)
                text = fuente.render(str(data[i][j]), True, black)
                screen.blit(text, (cell.x + cell.width / 2 - text.get_width() / 2, cell.y + cell.height / 2 - text.get_height() / 2))
        

# def imprimir_matriz(matriz):
#     for fila in matriz:
#         for valor in fila:
#             print(valor, end=' ')
#         print()

def crearTabla(grupo):
    matriz = [['Equipo','PJ','PG','PE','PP','GF','GC','Puntos']]
    for team in grupo:
        team_data = [team.get_name(), team.get_games_played(), team.get_games_won(), team.get_games_tied(), team.get_games_losed(), team.get_goals_favor(), team.get_goals_against(), team.get_points()]
        matriz.append(team_data)
        
        
    return matriz

def crearTabla1(teams):
    table = []
    for team in teams:
        team_data = [team[0], team[1], team[2], team[3], team[4], team[5], team[6], team[7]]
        table.append(team_data)
    return table

textos = [False,False,False,False,False,False,False,False]
tournament = Tournament()



resultados = {
    'grupoA': ['Partido aún sin jugar'] * 6,
    'grupoB': ['Partido aún sin jugar'] * 6,
    'grupoC': ['Partido aún sin jugar'] * 6,
    'grupoD': ['Partido aún sin jugar'] * 6,
    'grupoE': ['Partido aún sin jugar'] * 6,
    'grupoF': ['Partido aún sin jugar'] * 6,
    'grupoG': ['Partido aún sin jugar'] * 6,
    'grupoH': ['Partido aún sin jugar'] * 6,
}

grupo_actual = ''

jornada_actualA = 0
jornada_actualB = 0
jornada_actualC = 0
jornada_actualD = 0
jornada_actualE = 0
jornada_actualF = 0
jornada_actualG = 0
jornada_actualH = 0

jornada_checked = False
desca = None


#-----------------------PYGAME-----------------------------------------------------

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True    
        if jornada_checked:
                eliminatoria = Eliminatoria()
                eliminatoria.eliminatorias(tournament)
                jornada_checked = False
        else:  
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if menu_rect.collidepoint(event.pos):
                        menu_active = not menu_active
                    elif menu_active:
                        for i, option in enumerate(menu_options):
                            if pygame.Rect(menu_rect.x, menu_rect.y + (i+1)*30, menu_rect.width, menu_rect.height).collidepoint(event.pos):
                                selected_option = option
                                menu_active = False
                                break
                    if groups.collidepoint(event.pos):
                        group_active = not group_active
                    elif group_active:
                        for i, option in enumerate(group_options):
                            if pygame.Rect(groups.x, groups.y + (i+1)*30, groups.width, groups.height).collidepoint(event.pos):
                                groupO = option
                                group_active = False
                                break
                    if cost_rect.collidepoint(event.pos):
                        cost_active = not cost_active
                    elif cost_active:
                        for i, option in enumerate(cost_options):
                            if pygame.Rect(cost_rect.x, cost_rect.y + (i+1)*30, cost_rect.width, cost_rect.height).collidepoint(event.pos):
                                cost_selected = option
                                cost_active = False
                                break
                    if pres_rect.collidepoint(event.pos):
                        pres_active = not pres_active
                    elif pres_active:
                        for i, option in enumerate(pres_options):
                            if pygame.Rect(pres_rect.x, pres_rect.y + (i+1)*30, pres_rect.width, pres_rect.height).collidepoint(event.pos):
                                pres_selected = option
                                pres_active = False
                                break
                    if sta_rect.collidepoint(event.pos):
                        sta_active = not sta_active
                    elif sta_active:
                        for i, option in enumerate(sta_options):
                            if pygame.Rect(sta_rect.x, sta_rect.y + (i+1)*30, sta_rect.width, sta_rect.height).collidepoint(event.pos):
                                sta_selected = option
                                sta_active = False
                                break
                    
            
                    if subir_archivo.collidepoint(event.pos):
                        file_path = filedialog.askopenfilename()  # Abrir el cuadro de diálogo de selección de archivos
                        if file_path:
                            # Copiar el archivo seleccionado a la carpeta de recursos
                            shutil.copy(file_path, os.path.join('resources', os.path.basename(file_path)))  
                            csv = file_path
                    
                    if ingresar_bandera.collidepoint(event.pos):
                        file_path = filedialog.askopenfilename()  # Abrir el cuadro de diálogo de selección de archivos
                        if file_path:
                            # Copiar el archivo seleccionado a la carpeta de recursos
                            shutil.copy(file_path, os.path.join('resources', 'banderas', os.path.basename(file_path)))  
                            bandera = os.path.join('resources', 'banderas', os.path.basename(file_path))  # Guardar la nueva ruta del archivo en la variable 'bandera'
                            banderas.insert(cont_banderas, os.path.join('resources', 'banderas', os.path.basename(file_path)))  # Insertar la ruta al inicio de la lista 'banderas'
                            cont_banderas += 1
                    

                    if input_box1.collidepoint(event.pos):
                        active_box = 1
                    elif input_box2.collidepoint(event.pos):
                        active_box = 2
                    elif input_box3.collidepoint(event.pos):
                        active_box = 3
                    elif input_box4.collidepoint(event.pos):
                        active_box = 4
                    elif input_box5.collidepoint(event.pos):
                        active_box = 5
                    else:
                        active_box = None
                    color = color_active if active else color_inactive


                    if ingresar.collidepoint(event.pos):
                        if not team_name or not groupO or not resistance or not force or not speed or not pres_selected or not csv:
                            pygame.display.set_caption('Por favor, rellena todos los campos para crear un equipo')
                        else:
                            team = Teams(team_name,groupO, resistance,force,speed,pres_selected,False,bandera,cost_selected,0,0,0,0,0,0,0,csv)
                            grupo = tournament.crear_grupos(team)
                            matriz = crearTabla(grupo)
                    
                    if simular.collidepoint(event.pos):
                        simular_f1 += 1
                        simularf2 = 1
                        simular_f[0] = True
                        if jornada_actualA > 2 and jornada_actualB > 2 and jornada_actualC > 2 and jornada_actualD > 2 and jornada_actualE > 2 and jornada_actualF > 2 and jornada_actualG > 2 and jornada_actualH > 2:
                            jornada_checked = True
                        

                    if boton_A.collidepoint(event.pos): #Detectar cuando no estén completas
                        matriz = crearTabla(tournament.grupoA)
                        matriz_ordenada = [matriz[0]] + sorted(matriz[1:], key=lambda team: int(team[-1]), reverse=True)
                        matriz = crearTabla1(matriz_ordenada)
                        grupo_actual = "grupoA"
                        if simular_f[0] == True:
                            textos[0] = True

                    if boton_B.collidepoint(event.pos):
                        matriz = crearTabla(tournament.grupoB)
                        matriz_ordenada = [matriz[0]] + sorted(matriz[1:], key=lambda team: int(team[-1]), reverse=True)
                        matriz = crearTabla1(matriz_ordenada)
                        grupo_actual = "grupoB"
                        if simular_f[0] == True:
                            textos[1] = True

                    if  boton_C.collidepoint(event.pos):
                        matriz = crearTabla(tournament.grupoC)
                        matriz_ordenada = [matriz[0]] + sorted(matriz[1:], key=lambda team: int(team[-1]), reverse=True)
                        matriz = crearTabla1(matriz_ordenada)
                        grupo_actual = "grupoC"
                        if simular_f[0] == True:
                            textos[2] = True

                    if  boton_D.collidepoint(event.pos):
                        matriz = crearTabla(tournament.grupoD)
                        matriz_ordenada = [matriz[0]] + sorted(matriz[1:], key=lambda team: int(team[-1]), reverse=True)
                        matriz = crearTabla1(matriz_ordenada)
                        grupo_actual = "grupoD"
                        if simular_f[0] == True:
                            textos[3] = True

                    if  boton_E.collidepoint(event.pos):
                        matriz = crearTabla(tournament.grupoE)
                        matriz_ordenada = [matriz[0]] + sorted(matriz[1:], key=lambda team: int(team[-1]), reverse=True)
                        matriz = crearTabla1(matriz_ordenada)
                        grupo_actual = "grupoE"
                        if simular_f[0] == True:
                            textos[4] = True

                    if  boton_F.collidepoint(event.pos):
                        matriz = crearTabla(tournament.grupoF)
                        matriz_ordenada = [matriz[0]] + sorted(matriz[1:], key=lambda team: int(team[-1]), reverse=True)
                        matriz = crearTabla1(matriz_ordenada)
                        grupo_actual = "grupoF"
                        if simular_f[0] == True:
                            textos[5] = True

                    if  boton_G.collidepoint(event.pos):
                        matriz = crearTabla(tournament.grupoG)
                        matriz_ordenada = [matriz[0]] + sorted(matriz[1:], key=lambda team: int(team[-1]), reverse=True)
                        matriz = crearTabla1(matriz_ordenada)
                        grupo_actual = "grupoG"
                        if simular_f[0] == True:
                            textos[6] = True

                    if  boton_H.collidepoint(event.pos):
                        matriz = crearTabla(tournament.grupoH)
                        matriz_ordenada = [matriz[0]] + sorted(matriz[1:], key=lambda team: int(team[-1]), reverse=True)
                        matriz = crearTabla1(matriz_ordenada)
                        grupo_actual = "grupoH"
                        if simular_f[0] == True:
                            textos[7] = True


                if event.type == pygame.KEYDOWN:
                    if active_box is not None:
                        if event.key == pygame.K_RETURN:
                            if active_box == 1:
                                team_name = text1
                            elif active_box == 2:
                                resistance = text2
                            elif active_box == 3:
                                force = text3
                            elif active_box == 4:
                                speed = text4
                            elif active_box == 5:
                                desca = text5
                        elif event.key == pygame.K_BACKSPACE:
                            if active_box == 1:
                                text1 = text1[:-1]
                            elif active_box == 2:
                                text2 = text2[:-1]
                            elif active_box == 3:
                                text3 = text3[:-1]
                            elif active_box == 4:
                                text4 = text4[:-1]
                            elif active_box == 5:
                                text5 = text5[:-1]
                        else:
                            if active_box == 1:
                                text1 += event.unicode
                            elif active_box == 2:
                                text2 += event.unicode
                            elif active_box == 3:
                                text3 += event.unicode
                            elif active_box == 4:
                                text4 += event.unicode
                            elif active_box == 5:
                                text5 += event.unicode
        
        
            
        screen.fill((255, 255, 255))

        if desca is not None:
            lista = [tournament.grupoA,tournament.grupoB,tournament.grupoC,tournament.grupoD,tournament.grupoE,tournament.grupoF,tournament.grupoG,tournament.grupoH]
            for grupo in lista:
                for equipo in grupo:
                    if desca == equipo.get_name():
                        equipo.set_points(0)
                        equipo.set_resistence(0)
                        equipo.set_strength(0)
                        equipo.set_speed(0)
                        equipo.set_precision("Descalificado")
                        desca = None
                        print(equipo.get_name())
                        print(equipo.get_resistence())

        if simular_f[0] == True:
            if textos[0] == True:
                if simularf2 == 1:
                    juegosA = tournament.permutacion_name([tournament.grupoA[0],tournament.grupoA[1],tournament.grupoA[2],tournament.grupoA[3]])
                    jornada_actualA += 1
                    textos[0] = False
                    simularf2 = 0
                    simular_f[0] = False

                    if jornada_actualA == 1:
                        partido = Partido(selected_option,sta_selected,juegosA[0][1],juegosA[0][2])
                        partido1 = Partido(selected_option,sta_selected,juegosA[1][1],juegosA[1][2])
                        resultados["grupoA"][0] = Partido.assign_winner(partido)
                        resultados["grupoA"][1] = Partido.assign_winner(partido1)
                        
                    if jornada_actualA == 2:
                        partido = Partido(selected_option,sta_selected,juegosA[2][1],juegosA[2][2])
                        partido1 = Partido(selected_option,sta_selected,juegosA[3][1],juegosA[3][2])
                        resultados["grupoA"][2] = Partido.assign_winner(partido)
                        resultados["grupoA"][3] = Partido.assign_winner(partido1)
                    
                    if jornada_actualA == 3:
                        partido = Partido(selected_option,sta_selected,juegosA[4][1],juegosA[4][2])
                        partido1 = Partido(selected_option,sta_selected,juegosA[5][1],juegosA[5][2])
                        resultados["grupoA"][4] = Partido.assign_winner(partido)
                        resultados["grupoA"][5] = Partido.assign_winner(partido1)
                    
        
            if textos[1] == True:
                if simularf2 == 1:
                    juegosB = tournament.permutacion_name([tournament.grupoB[0],tournament.grupoB[1],tournament.grupoB[2],tournament.grupoB[3]])
                    jornada_actualB += 1
                    textos[1] = False
                    simularf2 = 0
                    simular_f[0] = False

                    if jornada_actualB == 1:
                        partido = Partido(selected_option,sta_selected,juegosB[0][1],juegosB[0][2])
                        partido1 = Partido(selected_option,sta_selected,juegosB[1][1],juegosB[1][2])
                        resultados["grupoB"][0] = Partido.assign_winner(partido)
                        resultados["grupoB"][1] = Partido.assign_winner(partido1)
                        
                    if jornada_actualB == 2:
                        partido = Partido(selected_option,sta_selected,juegosB[2][1],juegosB[2][2])
                        partido1 = Partido(selected_option,sta_selected,juegosB[3][1],juegosB[3][2])
                        resultados["grupoB"][2] = Partido.assign_winner(partido)
                        resultados["grupoB"][3] = Partido.assign_winner(partido1)
                    
                    if jornada_actualB == 3:
                        partido = Partido(selected_option,sta_selected,juegosB[4][1],juegosB[4][2])
                        partido1 = Partido(selected_option,sta_selected,juegosB[5][1],juegosB[5][2])
                        resultados["grupoB"][4] = Partido.assign_winner(partido)
                        resultados["grupoB"][5] = Partido.assign_winner(partido1)
            
            if textos[2] == True:
                if simularf2 == 1:
                    juegosC = tournament.permutacion_name([tournament.grupoC[0],tournament.grupoC[1],tournament.grupoC[2],tournament.grupoC[3]])
                    jornada_actualC += 1
                    textos[2] = False
                    simularf2 = 0
                    simular_f[0] = False

                    if jornada_actualC == 1:
                        partido = Partido(selected_option,sta_selected,juegosC[0][1],juegosC[0][2])
                        partido1 = Partido(selected_option,sta_selected,juegosC[1][1],juegosC[1][2])
                        resultados["grupoC"][0] = Partido.assign_winner(partido)
                        resultados["grupoC"][1] = Partido.assign_winner(partido1)
                        
                    if jornada_actualC == 2:
                        partido = Partido(selected_option,sta_selected,juegosC[2][1],juegosC[2][2])
                        partido1 = Partido(selected_option,sta_selected,juegosC[3][1],juegosC[3][2])
                        resultados["grupoC"][2] = Partido.assign_winner(partido)
                        resultados["grupoC"][3] = Partido.assign_winner(partido1)
                    
                    if jornada_actualC == 3:
                        partido = Partido(selected_option,sta_selected,juegosC[4][1],juegosC[4][2])
                        partido1 = Partido(selected_option,sta_selected,juegosC[5][1],juegosC[5][2])
                        resultados["grupoC"][4] = Partido.assign_winner(partido)
                        resultados["grupoC"][5] = Partido.assign_winner(partido1)

            if textos[3] == True:
                if simularf2 == 1:
                    juegosD = tournament.permutacion_name([tournament.grupoD[0],tournament.grupoD[1],tournament.grupoD[2],tournament.grupoD[3]])
                    jornada_actualD += 1
                    textos[3] = False
                    simularf2 = 0
                    simular_f[0] = False

                    if jornada_actualD == 1:
                        partido = Partido(selected_option,sta_selected,juegosD[0][1],juegosD[0][2])
                        partido1 = Partido(selected_option,sta_selected,juegosD[1][1],juegosD[1][2])
                        resultados["grupoD"][0] = Partido.assign_winner(partido)
                        resultados["grupoD"][1] = Partido.assign_winner(partido1)
                        
                    if jornada_actualD == 2:
                        partido = Partido(selected_option,sta_selected,juegosD[2][1],juegosD[2][2])
                        partido1 = Partido(selected_option,sta_selected,juegosD[3][1],juegosD[3][2])
                        resultados["grupoD"][2] = Partido.assign_winner(partido)
                        resultados["grupoD"][3] = Partido.assign_winner(partido1)
                    
                    if jornada_actualD == 3:
                        partido = Partido(selected_option,sta_selected,juegosD[4][1],juegosD[4][2])
                        partido1 = Partido(selected_option,sta_selected,juegosD[5][1],juegosD[5][2])
                        resultados["grupoD"][4] = Partido.assign_winner(partido)
                        resultados["grupoD"][5] = Partido.assign_winner(partido1)

            if textos[4] == True:
                if simularf2 == 1:
                    juegosE = tournament.permutacion_name([tournament.grupoE[0],tournament.grupoE[1],tournament.grupoE[2],tournament.grupoE[3]])
                    jornada_actualE += 1
                    textos[4] = False
                    simularf2 = 0
                    simular_f[0] = False

                    if jornada_actualE == 1:
                        partido = Partido(selected_option,sta_selected,juegosE[0][1],juegosE[0][2])
                        partido1 = Partido(selected_option,sta_selected,juegosE[1][1],juegosE[1][2])
                        resultados["grupoE"][0] = Partido.assign_winner(partido)
                        resultados["grupoE"][1] = Partido.assign_winner(partido1)
                        
                    if jornada_actualE == 2:
                        partido = Partido(selected_option,sta_selected,juegosE[2][1],juegosE[2][2])
                        partido1 = Partido(selected_option,sta_selected,juegosE[3][1],juegosE[3][2])
                        resultados["grupoE"][2] = Partido.assign_winner(partido)
                        resultados["grupoE"][3] = Partido.assign_winner(partido1)
                    
                    if jornada_actualE == 3:
                        partido = Partido(selected_option,sta_selected,juegosE[4][1],juegosE[4][2])
                        partido1 = Partido(selected_option,sta_selected,juegosE[5][1],juegosE[5][2])
                        resultados["grupoE"][4] = Partido.assign_winner(partido)
                        resultados["grupoE"][5] = Partido.assign_winner(partido1)

            if textos[5] == True:
                if simularf2 == 1:
                    juegosF = tournament.permutacion_name([tournament.grupoF[0],tournament.grupoF[1],tournament.grupoF[2],tournament.grupoF[3]])
                    jornada_actualF += 1
                    textos[5] = False
                    simularf2 = 0
                    simular_f[0] = False

                    if jornada_actualF == 1:
                        partido = Partido(selected_option,sta_selected,juegosF[0][1],juegosF[0][2])
                        partido1 = Partido(selected_option,sta_selected,juegosF[1][1],juegosF[1][2])
                        resultados["grupoF"][0] = Partido.assign_winner(partido)
                        resultados["grupoF"][1] = Partido.assign_winner(partido1)
                        
                    if jornada_actualF == 2:
                        partido = Partido(selected_option,sta_selected,juegosF[2][1],juegosF[2][2])
                        partido1 = Partido(selected_option,sta_selected,juegosF[3][1],juegosF[3][2])
                        resultados["grupoF"][2] = Partido.assign_winner(partido)
                        resultados["grupoF"][3] = Partido.assign_winner(partido1)
                    
                    if jornada_actualF == 3:
                        partido = Partido(selected_option,sta_selected,juegosF[4][1],juegosF[4][2])
                        partido1 = Partido(selected_option,sta_selected,juegosF[5][1],juegosF[5][2])
                        resultados["grupoF"][4] = Partido.assign_winner(partido)
                        resultados["grupoF"][5] = Partido.assign_winner(partido1)

            if textos[6] == True:
                if simularf2 == 1:
                    juegosG = tournament.permutacion_name([tournament.grupoG[0],tournament.grupoG[1],tournament.grupoG[2],tournament.grupoG[3]])
                    jornada_actualG += 1
                    textos[6] = False
                    simularf2 = 0
                    simular_f[0] = False

                    if jornada_actualG == 1:
                        partido = Partido(selected_option,sta_selected,juegosG[0][1],juegosG[0][2])
                        partido1 = Partido(selected_option,sta_selected,juegosG[1][1],juegosG[1][2])
                        resultados["grupoG"][0] = Partido.assign_winner(partido)
                        resultados["grupoG"][1] = Partido.assign_winner(partido1)
                        
                    if jornada_actualG == 2:
                        partido = Partido(selected_option,sta_selected,juegosG[2][1],juegosG[2][2])
                        partido1 = Partido(selected_option,sta_selected,juegosG[3][1],juegosG[3][2])
                        resultados["grupoG"][2] = Partido.assign_winner(partido)
                        resultados["grupoG"][3] = Partido.assign_winner(partido1)
                    
                    if jornada_actualG == 3:
                        partido = Partido(selected_option,sta_selected,juegosG[4][1],juegosG[4][2])
                        partido1 = Partido(selected_option,sta_selected,juegosG[5][1],juegosG[5][2])
                        resultados["grupoG"][4] = Partido.assign_winner(partido)
                        resultados["grupoG"][5] = Partido.assign_winner(partido1)
            
            if textos[7] == True:
                if simularf2 == 1:
                    juegosH = tournament.permutacion_name([tournament.grupoH[0],tournament.grupoH[1],tournament.grupoH[2],tournament.grupoH[3]])
                    jornada_actualH += 1
                    textos[7] = False
                    simularf2 = 0
                    simular_f[0] = False

                    if jornada_actualH == 1:
                        partido = Partido(selected_option,sta_selected,juegosH[0][1],juegosH[0][2])
                        partido1 = Partido(selected_option,sta_selected,juegosH[1][1],juegosH[1][2])
                        resultados["grupoH"][0] = Partido.assign_winner(partido)
                        resultados["grupoH"][1] = Partido.assign_winner(partido1)
                        
                    if jornada_actualH == 2:
                        partido = Partido(selected_option,sta_selected,juegosH[2][1],juegosH[2][2])
                        partido1 = Partido(selected_option,sta_selected,juegosH[3][1],juegosH[3][2])
                        resultados["grupoH"][2] = Partido.assign_winner(partido)
                        resultados["grupoH"][3] = Partido.assign_winner(partido1)
                    
                    if jornada_actualH == 3:
                        partido = Partido(selected_option,sta_selected,juegosH[4][1],juegosH[4][2])
                        partido1 = Partido(selected_option,sta_selected,juegosH[5][1],juegosH[5][2])
                        resultados["grupoH"][4] = Partido.assign_winner(partido)
                        resultados["grupoH"][5] = Partido.assign_winner(partido1)
        
        


    #-------------------------------RESULTADOS-------------------------------------------

        if grupo_actual == "grupoA":
            if jornada_actualA >= 1:
                txt_surface01 = pygame.font.Font(None, 20).render(resultados["grupoA"][0], True, (0, 0, 0))
                screen.blit(txt_surface01, (463, 455))
                txt_surface02 = pygame.font.Font(None, 20).render(resultados["grupoA"][1], True, (0, 0, 0))
                screen.blit(txt_surface02, (463, 485))
            if jornada_actualA >= 2:
                txt_surface03 = pygame.font.Font(None, 20).render(resultados["grupoA"][2], True, (0, 0, 0))
                screen.blit(txt_surface03, (713, 455))
                txt_surface04 = pygame.font.Font(None, 20).render(resultados["grupoA"][3], True, (0, 0, 0))
                screen.blit(txt_surface04, (713, 485))
            if jornada_actualA >= 3:
                txt_surface05 = pygame.font.Font(None, 20).render(resultados["grupoA"][4], True, (0, 0, 0))
                screen.blit(txt_surface05, (963, 455))
                txt_surface06 = pygame.font.Font(None, 20).render(resultados["grupoA"][5], True, (0, 0, 0))
                screen.blit(txt_surface06, (963, 485))

        elif grupo_actual == "grupoB":
            if jornada_actualB >= 1:
                txt_surface01 = pygame.font.Font(None, 20).render(resultados["grupoB"][0], True, (0, 0, 0))
                screen.blit(txt_surface01, (463, 455))
                txt_surface02 = pygame.font.Font(None, 20).render(resultados["grupoB"][1], True, (0, 0, 0))
                screen.blit(txt_surface02, (463, 485))
            if jornada_actualB >= 2:
                txt_surface03 = pygame.font.Font(None, 20).render(resultados["grupoB"][2], True, (0, 0, 0))
                screen.blit(txt_surface03, (713, 455))
                txt_surface04 = pygame.font.Font(None, 20).render(resultados["grupoB"][3], True, (0, 0, 0))
                screen.blit(txt_surface04, (713, 485))
            if jornada_actualB >= 3:
                txt_surface05 = pygame.font.Font(None, 20).render(resultados["grupoB"][4], True, (0, 0, 0))
                screen.blit(txt_surface05, (963, 455))
                txt_surface06 = pygame.font.Font(None, 20).render(resultados["grupoB"][5], True, (0, 0, 0))
                screen.blit(txt_surface06, (963, 485))
        
        elif grupo_actual == "grupoC":
            if jornada_actualC >= 1:
                txt_surface01 = pygame.font.Font(None, 20).render(resultados["grupoC"][0], True, (0, 0, 0))
                screen.blit(txt_surface01, (463, 455))
                txt_surface02 = pygame.font.Font(None, 20).render(resultados["grupoC"][1], True, (0, 0, 0))
                screen.blit(txt_surface02, (463, 485))
            if jornada_actualC >= 2:
                txt_surface03 = pygame.font.Font(None, 20).render(resultados["grupoC"][2], True, (0, 0, 0))
                screen.blit(txt_surface03, (713, 455))
                txt_surface04 = pygame.font.Font(None, 20).render(resultados["grupoC"][3], True, (0, 0, 0))
                screen.blit(txt_surface04, (713, 485))
            if jornada_actualC >= 3:
                txt_surface05 = pygame.font.Font(None, 20).render(resultados["grupoC"][4], True, (0, 0, 0))
                screen.blit(txt_surface05, (963, 455))
                txt_surface06 = pygame.font.Font(None, 20).render(resultados["grupoC"][5], True, (0, 0, 0))
                screen.blit(txt_surface06, (963, 485))
        
        elif grupo_actual == "grupoD":
            if jornada_actualD >= 1:
                txt_surface01 = pygame.font.Font(None, 20).render(resultados["grupoD"][0], True, (0, 0, 0))
                screen.blit(txt_surface01, (463, 455))
                txt_surface02 = pygame.font.Font(None, 20).render(resultados["grupoD"][1], True, (0, 0, 0))
                screen.blit(txt_surface02, (463, 485))
            if jornada_actualD >= 2:
                txt_surface03 = pygame.font.Font(None, 20).render(resultados["grupoD"][2], True, (0, 0, 0))
                screen.blit(txt_surface03, (713, 455))
                txt_surface04 = pygame.font.Font(None, 20).render(resultados["grupoD"][3], True, (0, 0, 0))
                screen.blit(txt_surface04, (713, 485))
            if jornada_actualD >= 3:
                txt_surface05 = pygame.font.Font(None, 20).render(resultados["grupoD"][4], True, (0, 0, 0))
                screen.blit(txt_surface05, (963, 455))
                txt_surface06 = pygame.font.Font(None, 20).render(resultados["grupoD"][5], True, (0, 0, 0))
                screen.blit(txt_surface06, (963, 485))
        
        elif grupo_actual == "grupoE":
            if jornada_actualE >= 1:
                txt_surface01 = pygame.font.Font(None, 20).render(resultados["grupoE"][0], True, (0, 0, 0))
                screen.blit(txt_surface01, (463, 455))
                txt_surface02 = pygame.font.Font(None, 20).render(resultados["grupoE"][1], True, (0, 0, 0))
                screen.blit(txt_surface02, (463, 485))
            if jornada_actualE >= 2:
                txt_surface03 = pygame.font.Font(None, 20).render(resultados["grupoE"][2], True, (0, 0, 0))
                screen.blit(txt_surface03, (713, 455))
                txt_surface04 = pygame.font.Font(None, 20).render(resultados["grupoE"][3], True, (0, 0, 0))
                screen.blit(txt_surface04, (713, 485))
            if jornada_actualE >= 3:
                txt_surface05 = pygame.font.Font(None, 20).render(resultados["grupoE"][4], True, (0, 0, 0))
                screen.blit(txt_surface05, (963, 455))
                txt_surface06 = pygame.font.Font(None, 20).render(resultados["grupoE"][5], True, (0, 0, 0))
                screen.blit(txt_surface06, (963, 485))
        
        elif grupo_actual == "grupoF":
            if jornada_actualF >= 1:
                txt_surface01 = pygame.font.Font(None, 20).render(resultados["grupoF"][0], True, (0, 0, 0))
                screen.blit(txt_surface01, (463, 455))
                txt_surface02 = pygame.font.Font(None, 20).render(resultados["grupoF"][1], True, (0, 0, 0))
                screen.blit(txt_surface02, (463, 485))
            if jornada_actualF >= 2:
                txt_surface03 = pygame.font.Font(None, 20).render(resultados["grupoF"][2], True, (0, 0, 0))
                screen.blit(txt_surface03, (713, 455))
                txt_surface04 = pygame.font.Font(None, 20).render(resultados["grupoF"][3], True, (0, 0, 0))
                screen.blit(txt_surface04, (713, 485))
            if jornada_actualF >= 3:
                txt_surface05 = pygame.font.Font(None, 20).render(resultados["grupoF"][4], True, (0, 0, 0))
                screen.blit(txt_surface05, (963, 455))
                txt_surface06 = pygame.font.Font(None, 20).render(resultados["grupoF"][5], True, (0, 0, 0))
                screen.blit(txt_surface06, (963, 485))

        elif grupo_actual == "grupoG":
            if jornada_actualG >= 1:
                txt_surface01 = pygame.font.Font(None, 20).render(resultados["grupoG"][0], True, (0, 0, 0))
                screen.blit(txt_surface01, (463, 455))
                txt_surface02 = pygame.font.Font(None, 20).render(resultados["grupoG"][1], True, (0, 0, 0))
                screen.blit(txt_surface02, (463, 485))
            if jornada_actualG >= 2:
                txt_surface03 = pygame.font.Font(None, 20).render(resultados["grupoG"][2], True, (0, 0, 0))
                screen.blit(txt_surface03, (713, 455))
                txt_surface04 = pygame.font.Font(None, 20).render(resultados["grupoG"][3], True, (0, 0, 0))
                screen.blit(txt_surface04, (713, 485))
            if jornada_actualG >= 3:
                txt_surface05 = pygame.font.Font(None, 20).render(resultados["grupoG"][4], True, (0, 0, 0))
                screen.blit(txt_surface05, (963, 455))
                txt_surface06 = pygame.font.Font(None, 20).render(resultados["grupoG"][5], True, (0, 0, 0))
                screen.blit(txt_surface06, (963, 485))
        
        elif grupo_actual == "grupoH":
            if jornada_actualH >= 1:
                txt_surface01 = pygame.font.Font(None, 20).render(resultados["grupoH"][0], True, (0, 0, 0))
                screen.blit(txt_surface01, (463, 455))
                txt_surface02 = pygame.font.Font(None, 20).render(resultados["grupoH"][1], True, (0, 0, 0))
                screen.blit(txt_surface02, (463, 485))
            if jornada_actualH >= 2:
                txt_surface03 = pygame.font.Font(None, 20).render(resultados["grupoH"][2], True, (0, 0, 0))
                screen.blit(txt_surface03, (713, 455))
                txt_surface04 = pygame.font.Font(None, 20).render(resultados["grupoH"][3], True, (0, 0, 0))
                screen.blit(txt_surface04, (713, 485))
            if jornada_actualH >= 3:
                txt_surface05 = pygame.font.Font(None, 20).render(resultados["grupoH"][4], True, (0, 0, 0))
                screen.blit(txt_surface05, (963, 455))
                txt_surface06 = pygame.font.Font(None, 20).render(resultados["grupoH"][5], True, (0, 0, 0))
                screen.blit(txt_surface06, (963, 485))
            
        txt_surface1 = font.render(text1, True, (0, 0, 0))
        screen.blit(input_text1, (input_box1.x-170, input_box1.y+5))
        screen.blit(txt_surface1, (input_box1.x+5, input_box1.y+2))
        pygame.draw.rect(screen, (22, 42, 130), input_box1, 2)

        txt_surface2 = font.render(text2, True, (0, 0, 0))
        screen.blit(input_text2, (input_box2.x-116, input_box2.y+5))
        screen.blit(txt_surface2, (input_box2.x+5, input_box2.y+2))
        pygame.draw.rect(screen, (0, 0, 0), input_box2, 2)

        txt_surface3 = font.render(text3, True, (0, 0, 0))
        screen.blit(input_text3, (input_box3.x-83, input_box3.y+5))
        screen.blit(txt_surface3, (input_box3.x+5, input_box3.y+2))
        pygame.draw.rect(screen, (0, 0, 0), input_box3, 2)

        txt_surface4 = font.render(text4, True, (0, 0, 0))
        screen.blit(input_text4, (input_box4.x-105, input_box4.y+5))
        screen.blit(txt_surface4, (input_box4.x+5, input_box4.y+2))
        pygame.draw.rect(screen, (0, 0, 0), input_box4, 2)

        txt_surface5 = font.render(text5, True, (0, 0, 0))
        screen.blit(input_text5, (input_box5.x-155, input_box5.y+2))
        screen.blit(txt_surface5, (input_box5.x+5, input_box5.y+2))
        pygame.draw.rect(screen, (0, 0, 0), input_box5, 2)
        
    #--------------------CONFIGURACION DE LOS MENUS DESPLEGABLES-----------------------------------------

        pygame.draw.rect(screen, (0, 0, 0), menu_rect, 2)
        menu_text = precisionF.render("Criterio", True, (0, 0, 0))
        screen.blit(menu_text, (menu_rect.x-75, menu_rect.y+2))
        
        pygame.draw.rect(screen, (0, 0, 0), groups, 2)
        group_text = font.render("Grupo" , True, (0, 0, 0))
        screen.blit(group_text, (groups.x-75, groups.y+2))

        pygame.draw.rect(screen, (0, 0, 0), cost_rect, 2)
        cost_text = precisionF.render("Costumbre de campo", True, (0, 0, 0))
        screen.blit(cost_text, (cost_rect.x-180, cost_rect.y+2))

        pygame.draw.rect(screen, (0, 0, 0), pres_rect, 2)
        pres_text = precisionF.render("Precision", True, (0, 0, 0))
        screen.blit(pres_text, (pres_rect.x-90, pres_rect.y+2))

        pygame.draw.rect(screen, (0, 0, 0), sta_rect, 2)
        sta_text = precisionF.render("Estadio", True, (0, 0, 0))
        screen.blit(sta_text, (sta_rect.x-90, sta_rect.y+2))
        
    #--------------------CONFIGURACION DE LOS BOTONES-----------------------------------------

        pygame.draw.rect(screen, black, border)
        pygame.draw.rect(screen, white, subir_archivo)
        button_text = font.render("Subir archivo", True, (0, 0, 0))
        screen.blit(button_text, (subir_archivo.x + 10, subir_archivo.y + 3))
        
        pygame.draw.rect(screen, black, border_ingresar)
        pygame.draw.rect(screen, white, ingresar)
        ingresar_text = font.render("Ingresar", True, (0, 0, 0))
        screen.blit(ingresar_text, (ingresar.x + 35, ingresar.y + 3))

        pygame.draw.rect(screen, black, border_ingresar_bandera)
        pygame.draw.rect(screen, white, ingresar_bandera)
        ingresar_bandera_text = font.render("Ingresar bandera", True, (0, 0, 0))
        screen.blit(ingresar_bandera_text, (ingresar_bandera.x+3, ingresar_bandera.y + 3))

        pygame.draw.rect(screen, black, boton_simular)
        pygame.draw.rect(screen, white, simular)
        simular_text = font.render("Simular fecha", True, (0, 0, 0))
        screen.blit(simular_text, (simular.x + 15, simular.y + 3))


        
        
    #----------------------------------TEXTOS---------------------------------------------


        txt_surface0 = pygame.font.Font(None, 35).render("TABLA DE PUNTOS", True, (0, 0, 0))
        screen.blit(txt_surface0, (600, 165))

        txt_surface0 = pygame.font.Font(None, 25).render("Resultados Jornada 1", True, (0, 0, 0))
        screen.blit(txt_surface0, (450, 425))

        txt_surface0 = pygame.font.Font(None, 25).render("Resultados Jornada 2", True, (0, 0, 0))
        screen.blit(txt_surface0, (700, 425))

        txt_surface0 = pygame.font.Font(None, 25).render("Resultados Jornada 3", True, (0, 0, 0))
        screen.blit(txt_surface0, (950, 425))

        

        pygame.draw.rect(screen, black, boton_A)
        pygame.draw.rect(screen, white, A)
        A_text = font.render("A", True, (0, 0, 0))
        screen.blit(A_text, (A.x + 15, A.y + 3))
        
        pygame.draw.rect(screen, black, boton_B)
        pygame.draw.rect(screen, white, B)
        B_text = font.render("B", True, (0, 0, 0))
        screen.blit(B_text, (B.x + 15, B.y + 3))

        pygame.draw.rect(screen, black, boton_C)
        pygame.draw.rect(screen, white, C)
        C_text = font.render("C", True, (0, 0, 0))
        screen.blit(C_text, (C.x + 15, C.y + 3))

        pygame.draw.rect(screen, black, boton_D)  
        pygame.draw.rect(screen, white, D)
        D_text = font.render("D", True, (0, 0, 0))
        screen.blit(D_text, (D.x + 15, D.y + 3))

        pygame.draw.rect(screen, black, boton_E)
        pygame.draw.rect(screen, white, E)
        E_text = font.render("E", True, (0, 0, 0))
        screen.blit(E_text, (E.x + 15, E.y + 3))

        pygame.draw.rect(screen, black, boton_F)
        pygame.draw.rect(screen, white, F)
        F_text = font.render("F", True, (0, 0, 0))
        screen.blit(F_text, (F.x + 15, F.y + 3))

        pygame.draw.rect(screen, black, boton_G)
        pygame.draw.rect(screen, white, G)
        G_text = font.render("G", True, (0, 0, 0))
        screen.blit(G_text, (G.x + 15, G.y + 3))

        pygame.draw.rect(screen, black, boton_H)
        pygame.draw.rect(screen, white, H)
        H_text = font.render("H", True, (0, 0, 0))
        screen.blit(H_text, (H.x + 15, H.y + 3))

    #--------------------CONFIGURACION DE LAS OPCIONES DE LOS MENUS-----------------------------------------
        
    # Dibujar las opciones del menú si el menú está activo
        if menu_active:
            for i, option in enumerate(menu_options):
                option_rect = pygame.Rect(menu_rect.x, menu_rect.y + (i+1)*30, menu_rect.width, menu_rect.height)
                pygame.draw.rect(screen, (0, 0, 0), option_rect, 1)
                option_text = font.render(option, True, (0, 0, 0))
                screen.blit(option_text, (option_rect.x+5, option_rect.y+3))
            
        if group_active:
            for i, option in enumerate(group_options):
                option_rect = pygame.Rect(groups.x, groups.y + (i+1)*30, groups.width, groups.height)
                pygame.draw.rect(screen, (0, 0, 0), option_rect, 1)
                option_text = font.render(option, True, (0, 0, 0))
                screen.blit(option_text, (option_rect.x+35, option_rect.y+1))

        if cost_active:
            for i, option in enumerate(cost_options):
                option_rect = pygame.Rect(cost_rect.x, cost_rect.y + (i+1)*27, cost_rect.width, cost_rect.height)
                pygame.draw.rect(screen, (0, 0, 0), option_rect, 1)
                option_text = font.render(option, True, (0, 0, 0))
                screen.blit(option_text, (option_rect.x+5, option_rect.y+2))
        
        if pres_active:
            for i, option in enumerate(pres_options):
                presi_rect = pygame.Rect(pres_rect.x, pres_rect.y + (i+1)*27, pres_rect.width, pres_rect.height)
                pygame.draw.rect(screen, (0, 0, 0), presi_rect, 1)
                pres_text = font.render(option, True, (0, 0, 0))
                screen.blit(pres_text, (presi_rect.x+5, presi_rect.y+2))
        
        if sta_active:
            for i, option in enumerate(sta_options):
                stad_rect = pygame.Rect(sta_rect.x, sta_rect.y + (i+1)*27, sta_rect.width, sta_rect.height)
                pygame.draw.rect(screen, (0, 0, 0), stad_rect, 1)
                sta_text = font.render(option, True, (0, 0, 0))
                screen.blit(sta_text, (stad_rect.x+5, stad_rect.y+2))


        draw_table(matriz) 
        pygame.display.flip()
pygame.quit()

