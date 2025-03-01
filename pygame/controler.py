from teams import Teams
from arboles import Nodo
from tournament import Tournament
from partido import Partido
import random
from diagrama import BarChart
#craecion de los equipos 
#se crea una instancia de torneo 

class Controler:

#genera un aleatorio entre medio alto y bajo
    def aleatorio_t(self):
        r= random.randint(1,3)
        if r==1:
            return "Alto"
        if r==2:
            return "Medio"
        if r==3:
            return "Bajo"
        
    #genera un aleatorio para el criterio
    def aleatorio_c(self):
        r= random.randint(1,4)
        if r==1:
            return "velocidad"
        if r==2:
            return "presicion"
        if r==3:
            return "fuerza"
        if r==4:
            return "resistencia"
        
    #juega los paridos correspondientes a un grupo
    def jugar_partidos(self,partidos):
        for p in partidos:
            if p[0] == "jornada 1":
                print("------jornada 1------")   
            if p[0] == "jornada 2":
                print("------jornada 2------")
            if p[0] == "jornada 3":
                print("-------jornada 3------")
            par= Partido(
                criterio= self.aleatorio_c(),
                terreno= self.aleatorio_t(),
                jugador1= p[1],
                jugador2= p[2]
            )
            print(par.assign_winner2()[1])
        print("-----------------------------------------")

    #permutaciones partidos del grupo 2
    
    def tuplas(self,permutacion, ronda):
        if ronda == 1:
            tupla= [[permutacion[0],permutacion[1]],[permutacion[2],permutacion[3]],[permutacion[4],permutacion[5]],[permutacion[6],permutacion[7]],[permutacion[8],permutacion[9]],[permutacion[10],permutacion[11]],[permutacion[12],permutacion[13]],[permutacion[14],permutacion[15]]]
            return tupla
        #apartir de aqui lo que ingresa en permutaciones son los ganadores
        if ronda == 2:
            tupla=[[permutacion[0],permutacion[1]],[permutacion[2],permutacion[3]],[permutacion[4],permutacion[5]],[permutacion[6],permutacion[7]]]
            return tupla
        if ronda == 3:
            tupla=[[permutacion[0],permutacion[1]],[permutacion[2],permutacion[3]]] 
            return tupla
            
    def agregar_plata(self, equipos, fase):
        if fase == 1:
            for e in equipos:
                e.set_dinero(20000)  # Agregamos una cantidad fija de dinero
        if fase == 2:
            for e in equipos:
                e.set_dinero(e.get_dinero() + 25000)  # Agregamos una cantidad fija de dinero
        if fase == 3:
            for e in equipos:
                e.set_dinero(e.get_dinero() + 35000)  # Agregamos una cantidad fija de dinero
        if fase == 4:
            for e in equipos:
                e.set_dinero(e.get_dinero() + 40000)  # Agregamos una cantidad fija de dinero
            
    def jugar_permutacion(self,permutaciones):
        self.agregar_plata(permutaciones,1)
        p= permutaciones
        tupla=self.tuplas(p,1)
        resultados=[]
        ganadores=[]
        ganadores2=[]
        ganadores3=[]
        
        for t in tupla:
            p1= Partido(
                criterio= self.aleatorio_c(),
                terreno= self.aleatorio_t(),
                jugador1=t[0],
                jugador2=t[1]    
            )
            resultados.append(p1.assign_winner2()[1])
            ganadores.append(p1.assign_winner2()[0])
        #agrego la plata    
        self.agregar_plata(ganadores,2)

        raiz= self.inicializar_arbol()
        raiz.construir_arbol(raiz,resultados)
        resultado=[]
        tupla2=self.tuplas(ganadores,2)
        for t in tupla2:
            p1= Partido(
                criterio= self.aleatorio_c(),
                terreno= self.aleatorio_t(),
                jugador1=t[0],
                jugador2=t[1]    
            )   
            resultados.append(p1.assign_winner2()[1])
            ganadores2.append(p1.assign_winner2()[0])
        #agrego la plata    
        self.agregar_plata(ganadores2,3)
        raiz.construir_arbol2(raiz,resultados)
        resultados=[]
        tupla3=self.tuplas(ganadores2,3)
        for t in tupla3:
            p1= Partido(
                criterio= self.aleatorio_c(),
                terreno= self.aleatorio_t(),
                jugador1=t[0],
                jugador2=t[1]    
            )
            resultados.append(p1.assign_winner2()[1])
            ganadores3.append(p1.assign_winner2()[0])
        #agrego la plata    
        self.agregar_plata(ganadores3,4)
        raiz.construir_arbol3(raiz,resultados)
        resultados=[]
        p1=Partido(
                criterio= self.aleatorio_c(),
                terreno= self.aleatorio_t(),
                jugador1=ganadores3[0],
                jugador2=ganadores3[1]    
            )
        resultado=p1.assign_winner2()[1]
        raiz.set_info(resultado)


        return raiz
        


    #inicializacion del arbol 
    def inicializar_arbol(self):
        raiz= Nodo(8)
        raiz= raiz.agregar(raiz,4)
        raiz= raiz.agregar(raiz,12)
        raiz= raiz.agregar(raiz,2)
        raiz= raiz.agregar(raiz,6)
        raiz= raiz.agregar(raiz,10)
        raiz= raiz.agregar(raiz,14)
        raiz= raiz.agregar(raiz,1)
        raiz= raiz.agregar(raiz,3)
        raiz= raiz.agregar(raiz,5)
        raiz= raiz.agregar(raiz,7)
        raiz= raiz.agregar(raiz,9)
        raiz= raiz.agregar(raiz,11)
        raiz= raiz.agregar(raiz,13)
        raiz= raiz.agregar(raiz,15)
        return raiz

    def crear_diagrama(self,permutacion):
        names=[permutacion[0].get_name(),permutacion[1].get_name(),permutacion[2].get_name(),permutacion[3].get_name(),permutacion[4].get_name(),permutacion[5].get_name(),permutacion[6].get_name(),permutacion[7].get_name(),permutacion[8].get_name(),permutacion[9].get_name(),permutacion[10].get_name(),permutacion[11].get_name(),permutacion[12].get_name(),permutacion[13].get_name(),permutacion[14].get_name(),permutacion[15].get_name()]
        valores=[permutacion[0].get_dinero(),permutacion[1].get_dinero(),permutacion[2].get_dinero(),permutacion[3].get_dinero(),permutacion[4].get_dinero(),permutacion[5].get_dinero(),permutacion[6].get_dinero(),permutacion[7].get_dinero(),permutacion[8].get_dinero(),permutacion[9].get_dinero(),permutacion[10].get_dinero(),permutacion[11].get_dinero(),permutacion[12].get_dinero(),permutacion[13].get_dinero(),permutacion[14].get_dinero(),permutacion[15].get_dinero()]
        print(permutacion[0].get_name())
        return names,valores



