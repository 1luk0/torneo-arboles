import csv

class Jugador:
    
 # calcula la altura promedio de un equipo en particular  
 #index 2 
    def altura_promedio(self,archivo, index):
        s=0
        
        with open(archivo, newline='') as csvfile:
            spamreader = csv.reader(csvfile)
            for row in spamreader:
                
                if index < len(row):
                    element = row[index]
                    if self.isNumeric(element):
                        s+= float(element)

            return(s/11)  
    #index 5      
    def mayor_salario(self, archivo, index):
        mayor = 0
        nombre_mayor = ''
        with open(archivo, newline='') as csvfile:
            spamreader = csv.reader(csvfile)
            for row in spamreader:
                if index < len(row):
                    element = row[index]
                    if self.isNumeric(element):
                        salario = float(element)
                        if salario > mayor:
                            mayor = salario
                            nombre_mayor = row[0]  # Asume que el nombre del jugador está en la columna 1
        return mayor, nombre_mayor

    #entran los objetos d elos equipos clasificados
    def mayor_altura(self,segunda_fase):
        mayor=0
        e_mayor=''
        for element in segunda_fase:
            equipo= './resources/' + str(element.get_name()) + '.csv'
            a= self.altura_promedio(equipo,2)
            if a > mayor:
                e_mayor=element.get_name()
                mayor = round(a, 2)  # Redondea 'a' a dos decimales antes de asignarlo a 'mayor'
        return "El mayor promedio de altura lo tiene el equipo de "+ str(e_mayor) + " con: " + str(mayor) +"m"

    def menor_altura(self,segunda_fase):
        menor=1000
        e_menor=''
        for element in segunda_fase:
            equipo= './resources/' + str(element.get_name()) + '.csv'
            a = self.altura_promedio(equipo,2)
            if a < menor:
                e_menor=element.get_name()
                menor = round(a, 2)
        return "El menor promedio de altura lo tiene el equipo de "+ str(e_menor) + " con: " + str(menor) +"m"

    #entran los que quedaron segundos en la primera fase
    def segundos_salario(self,segundos):
        mayor_s=0
        jugador_m=''
        for element in segundos:
            equipo= './resources/' + str(element.get_name()) + '.csv'
            salary= self.mayor_salario(equipo,4)
            if salary[0] > mayor_s:
                jugador_m=salary[1]
                mayor_s=salary[0]
        return "El mayor salario lo tiene el jugador "+ str(jugador_m) + " con: " + str(mayor_s) +"M"

    def sacar_segundos(self,clasificados) :
        segundos=[]
        for i in range(15):
            if i%2 != 0:
                segundos.append(clasificados[i])
        return segundos
            
                    
    #es numero o no 
    def isNumeric(self,s):
        try:
            float(s)
            return True
        except ValueError:
            return False
    
    

    