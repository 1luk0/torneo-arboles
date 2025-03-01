from teams import Teams
from partido import Partido
import itertools

class Tournament:
    
    def __init__(self):
        self.grupoA = []
        self.grupoB = []
        self.grupoC = []
        self.grupoD = []
        self.grupoE = []
        self.grupoF = []
        self.grupoG = []
        self.grupoH = []
    
    def get_equipo(self, nombre):
        for grupo in [self.grupoA, self.grupoB, self.grupoC, self.grupoD, self.grupoE, self.grupoF, self.grupoG, self.grupoH]:
            for equipo in grupo:
                if equipo.get_name() == nombre:
                    return equipo
        return None
        
    
    def get__grupoA(self):
        return self.grupoA
    def get__grupoB(self):
        return self.grupoB
    def get__grupoC(self):
        return self.grupoC
    def get__grupoD(self):
        return self.grupoD
    def get__grupoE(self):
        return self.grupoE
    def get__grupoF(self):
        return self.grupoF
    def get__grupoG(self):
        return self.grupoG
    def get__grupoH(self):
        return self.grupoH
     

    def crear_grupos(self,equipo):
        if equipo.get_group()=='Grupo A':
            self.grupoA.append(equipo)
            return self.grupoA
        if equipo.get_group()=='Grupo B':
            self.grupoB.append(equipo)
            return self.grupoB
        if equipo.get_group()=='Grupo C':
            self.grupoC.append(equipo)
            return self.grupoC
        if equipo.get_group()=='Grupo D':
            self.grupoD.append(equipo)
            return self.grupoD
        if equipo.get_group()=='Grupo E':
            self.grupoE.append(equipo)
            return self.grupoE
        if equipo.get_group()=='Grupo F':
            self.grupoF.append(equipo)
            return self.grupoF
        if equipo.get_group()=='Grupo G':
            self.grupoG.append(equipo)
            return self.grupoG
        if equipo.get_group()=='Grupo H':
            self.grupoH.append(equipo)
            return self.grupoH

     
     
     
     
    def permutacion_name(self,grupo):
        partidos=[0,0,0,0,0,0]
        partidos[0]=("jornada 1",grupo[0],grupo[3])
        partidos[1]=("jornada 1",grupo[1],grupo[2])
        partidos[2]=("jornada 2",grupo[0],grupo[2])
        partidos[3]=("jornada 2",grupo[1],grupo[3])
        partidos[4]=("jornada 3",grupo[0],grupo[1])
        partidos[5]=("jornada 3",grupo[2],grupo[3])

        return partidos
    
    #hace lo mismoq ue la funcion anterior pero en lugar de devolver solo el nombre devuelve el objeto completo
    def permutacion_objeto(self, grupo):
        partidos=[0,0,0,0,0,0]
        partidos[0]=["jornada 1",grupo[0],grupo[3]]
        partidos[1]=["jornada 1",grupo[1],grupo[2]]
        partidos[2]=["jornada 2",grupo[0],grupo[2]]
        partidos[3]=["jornada 2",grupo[1],grupo[3]]
        partidos[4]=["jornada 3",grupo[0],grupo[1]]
        partidos[5]=["jornada 3",grupo[2],grupo[3]]
        return partidos
    
    #permutaciones partidos del grupo 2
    #permutaciones partidos del grupo 2
    def permutaciones_arbol(self,clasificados_grupo1, clasificados_grupo2,index):
        permutaciones1= list(itertools.permutations(clasificados_grupo1))
        permutaciones2= list(itertools.permutations(clasificados_grupo2))
        p1= list(permutaciones1[index])
        p2=list(permutaciones2[index])
        permutacion= p1+p2
        return permutacion
    
    
            

    #DEVUELVE UNA LISTA CON LOS DOS CLASIFICADOS DE CADA GRUPO ORDENADOS DE A-H
    def clasificados_grupo(self):
        #creamos una lista
        lista=[]
        #obtengo el grupo a
        A=self.get__grupoA()
        # obtengo los puntos de los equipos
        Apuntos= [A[0].get_points(),A[1].get_points(), A[2].get_points(),A[3].get_points()]
        #maximo de esa lista
        maximo= max(Apuntos)
        #el indice en el que esta ese maximo
        ind1 = Apuntos.index(maximo)
        #borramos ese maximo para hallar el siguiente maximo
        del Apuntos[ind1]
        #repetimos el proceso
        maximo2= max(Apuntos)
        ind2= Apuntos.index(maximo2)
        #asignamos a la lista los equipos con mayor puntaje 
        lista.append(A[ind1])
        lista.append(A[ind2])
        #Grupo B
        B= self.get__grupoB()
        Bpuntos=[B[0].get_points(),B[1].get_points(), B[2].get_points(),B[3].get_points()]
        maximo= max(Bpuntos)
        ind1=Bpuntos.index(maximo)
        del Bpuntos [ind1]
        maximo2= max(Bpuntos)
        ind2= Bpuntos.index(maximo2)
        lista.append(B[ind1])
        lista.append(B[ind2])
        #Grupo C
        C= self.get__grupoC()
        Cpuntos=[C[0].get_points(),C[1].get_points(), C[2].get_points(),C[3].get_points()]
        maximo= max(Cpuntos)
        ind1= Cpuntos.index(maximo)
        del Cpuntos[ind1]
        maximo2= max(Cpuntos)
        ind2= Cpuntos.index(maximo2)
        lista.append(C[ind1])
        lista.append(C[ind2])
        #Grupo D
        D= self.get__grupoD()
        Dpuntos=[D[0].get_points(),D[1].get_points(), D[2].get_points(),D[3].get_points()]
        maximo= max(Dpuntos)
        ind1=Dpuntos.index(maximo)
        del Dpuntos[ind1]
        maximo2= max(Dpuntos)
        ind2= Dpuntos.index(maximo2)
        lista.append(D[ind1])
        lista.append(D[ind2])
        #Grupo E
        E= self.get__grupoE()
        Epuntos=[E[0].get_points(),E[1].get_points(), E[2].get_points(),E[3].get_points()]
        maximo= max(Epuntos)
        ind1=Epuntos.index(maximo)
        del Epuntos[ind1]
        maximo2= max(Epuntos)
        ind2= Epuntos.index(maximo2)
        lista.append(E[ind1])
        lista.append(E[ind2])
        #Grupo F
        F= self.get__grupoF()
        Fpuntos=[F[0].get_points(),F[1].get_points(), F[2].get_points(),F[3].get_points()]
        maximo= max(Fpuntos)
        ind1=Fpuntos.index(maximo)
        del Fpuntos[ind1]
        maximo2= max(Fpuntos)
        ind2= Fpuntos.index(maximo2)
        lista.append(F[ind1])
        lista.append(F[ind2])
        #grupo G
        G= self.get__grupoG()
        Gpuntos=[G[0].get_points(),G[1].get_points(), G[2].get_points(),G[3].get_points()]
        maximo= max(Gpuntos)
        ind1=Gpuntos.index(maximo)
        del Gpuntos[ind1]
        maximo2= max(Gpuntos)
        ind2= Gpuntos.index(maximo2)
        lista.append(G[ind1])
        lista.append(G[ind2])
        #Grupo H
        H= self.get__grupoH()
        Hpuntos=[H[0].get_points(),H[1].get_points(), H[2].get_points(),H[3].get_points()]
        maximo= max(Hpuntos)
        ind1=Hpuntos.index(maximo)
        del Hpuntos[ind1]
        maximo2= max(Hpuntos)
        ind2= Hpuntos.index(maximo2)
        lista.append(H[ind1])
        lista.append(H[ind2])

        return lista
    nums=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
    

    










