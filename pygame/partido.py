from teams  import Teams
import random
class Partido:
     goles_totales = 0

     def __init__(self,criterio=None, terreno=None, jugador1=None, jugador2=None):
          self.__criterio= criterio
          self.__terreno= terreno
          self.__jugador1=jugador1
          self.__jugador2= jugador2
          self.goles_contados = False

    
     # Getters
     def get_criterio(self):
         return self.__criterio
    
     def get_terreno(self):
         if self.__terreno =="Alto":
             return 1 
         elif self.__terreno =="Medio":
             return 2
         elif self.__terreno =="Bajo":
             return 3
     
     def get_jugador1(self):
          return self.__jugador1
     
     def get_jugador2(self):
         return self.__jugador2
     
      # Setters
     def set_criterio(self, criterio):
          self.__criterio= criterio

     def set_terreno(self, terreno):
          if terreno =="Alto":
            self.__terreno = 1
          elif terreno =="Medio":
            self.__terreno = 2
          elif terreno =="Bajo":
            self.__terreno == 3

     def set_jugador1(self, jugador1):
         self.__jugador1 = jugador1
     def set_jugador2(self, jugador2):
         self.__jugador2 = jugador2

     def empate(self):
        emp = random.randint(0, 3)
        return emp
    
     def ganador(self,g):
        if g > 0:
            gan = random.randint(1, g)
            return gan
        else:
            return 0
        
     def tied_table(self,team1,team2,emp):
         team1.set_points(team1.get_points()+1)
         team2.set_points(team2.get_points()+1)
         team1.set_games_tied(team1.get_games_tied()+1)
         team2.set_games_tied(team2.get_games_tied()+1)
         team1.set_goals_against(team1.get_goals_against()+emp)
         team1.set_goals_favor(team1.get_goals_favor()+emp)
         team2.set_goals_against(team2.get_goals_against()+emp)
         team2.set_goals_favor(team2.get_goals_favor()+emp)
         team1.set_games_played(team1.get_games_played()+1)
         team2.set_games_played(team2.get_games_played()+1)
    
     def win_table1(self,team1,team2,gan,per):
         team1.set_games_played(team1.get_games_played()+1)
         team2.set_games_played(team2.get_games_played()+1)
         team1.set_points(team1.get_points()+3)
         team1.set_games_won(team1.get_games_won()+1)
         team2.set_games_losed(team2.get_games_losed()+1)
         team1.set_goals_against(team1.get_goals_against()+per)
         team1.set_goals_favor(team1.get_goals_favor()+gan)
         team2.set_goals_against(team2.get_goals_against()+gan)
         team2.set_goals_favor(team2.get_goals_favor()+per)
    
     def win_table2(self,team1,team2,gan,per):
         team1.set_games_played(team1.get_games_played()+1)
         team2.set_games_played(team2.get_games_played()+1)
         team2.set_points(team2.get_points()+3)
         team2.set_games_won(team2.get_games_won()+1)
         team1.set_games_losed(team1.get_games_losed()+1)
         team2.set_goals_against(team2.get_goals_against()+per)
         team2.set_goals_favor(team2.get_goals_favor()+gan)
         team1.set_goals_against(team1.get_goals_favor()+gan)
         team1.set_goals_favor(team1.get_goals_favor()+per)

     def ventaja_terreno(self):
         v=0
         if (self.get_jugador1().get_costumbre_terreno()) - self.get_jugador2().get_costumbre_terreno()== 2 or (self.get_jugador1().get_costumbre_terreno() - self.get_jugador2().get_costumbre_terreno())== -2:
             if self.get_jugador1().get_costumbre_terreno() == self.get_terreno():
                 v= [0.3,0]
             elif self.get_jugador2().get_costumbre_terreno() == self.get_terreno():
                 v=[0, 0.3]
             else:
                 v=[0,0]
         elif (self.get_jugador1().get_costumbre_terreno() - self.get_jugador2().get_costumbre_terreno())==1 or (self.get_jugador1().get_costumbre_terreno() - self.get_jugador2().get_costumbre_terreno())==-1:
             if self.get_jugador1().get_costumbre_terreno() == self.get_terreno():
                 v=[ 0.2,0]
             elif self.get_jugador2().get_costumbre_terreno() == self.get_terreno():
                 v=[0, 0.2]
             elif (self.get_jugador1().get_costumbre_terreno()-self.get_terreno())==2 or(self.get_jugador1().get_costumbre_terreno()-self.get_terreno())==-2:
                 v=[0.1,0]
             else:
                 v=[0,0.1]
         elif (self.get_jugador1().get_costumbre_terreno() - self.get_jugador2().get_costumbre_terreno())==0:
             v=[0,0]
         return v
     
     

     def ventaja_terreno(self):
         v=0
         if (self.get_jugador1().get_costumbre_terreno()) - self.get_jugador2().get_costumbre_terreno()== 2 or (self.get_jugador1().get_costumbre_terreno() - self.get_jugador2().get_costumbre_terreno())== -2:
             if self.get_jugador1().get_costumbre_terreno() == self.get_terreno():
                 v= [0.3,0]
             elif self.get_jugador2().get_costumbre_terreno() == self.get_terreno():
                 v=[0, 0.3]
             else:
                 v=[0,0]
         elif (self.get_jugador1().get_costumbre_terreno() - self.get_jugador2().get_costumbre_terreno())==1 or (self.get_jugador1().get_costumbre_terreno() - self.get_jugador2().get_costumbre_terreno())==-1:
             if self.get_jugador1().get_costumbre_terreno() == self.get_terreno():
                 v=[ 0.2,0]
             elif self.get_jugador2().get_costumbre_terreno() == self.get_terreno():
                 v=[0, 0.2]
             elif (self.get_jugador1().get_costumbre_terreno()-self.get_terreno())==2 or(self.get_jugador1().get_costumbre_terreno()-self.get_terreno())==-2:
                 v=[0.1,0]
             else:
                 v=[0,0.1]
         elif (self.get_jugador1().get_costumbre_terreno() - self.get_jugador2().get_costumbre_terreno())==0:
             v=[0,0]
         return v
     
     

     def assign_winner(self): #Se deben cambiar los condicionales para que estos sean las opciones marcadas en el pygame y los returns 
        gan = self.ganador(5)
        per = self.ganador(gan-1) 
        empate = self.empate()
        ventaja = self.ventaja_terreno()
        if self.get_criterio() == "resistencia": #cambiar con pygame
            if int(self.get_jugador1().get_resistence()) + int(self.get_jugador1().get_resistence()) * ventaja[0] == int(self.get_jugador2().get_resistence()) + int(self.get_jugador2().get_resistence()) * ventaja[1]:
                if int(self.get_jugador1().get_strength()) + int(self.get_jugador1().get_strength()) * ventaja[0] == int(self.get_jugador2().get_strength()) + int(self.get_jugador2().get_strength()) * ventaja[1]:
                    self.tied_table(self.get_jugador1(), self.get_jugador2(), empate)
                    return (self.get_jugador1().get_name() + ' (' + str(empate) + ')' + ' VS ' +  self.get_jugador2().get_name() +' (' + str(empate) + ')')
                    
                else:
                    if int(self.get_jugador1().get_strength()) + int(self.get_jugador1().get_strength()) * ventaja[0] > int(self.get_jugador2().get_strength()) + int(self.get_jugador2().get_strength()) * ventaja[1]:
                        self.win_table1(self.get_jugador1(), self.get_jugador2(), gan, per) #Optimizar
                        return (self.get_jugador1().get_name() + ' (' + str(gan) + ')' + ' VS ' + self.get_jugador2().get_name() +' (' + str(per) + ')')
                        
                    else:
                        self.win_table2(self.get_jugador1(), self.get_jugador2(), gan, per) #OPtimizar
                        return (self.get_jugador1().get_name() + ' (' + str(per) + ')' + ' VS ' + self.get_jugador2().get_name() +' (' + str(gan) + ')')
                        
                
            else:
                if int(self.get_jugador1().get_resistence()) + int(self.get_jugador1().get_resistence()) * ventaja[0] > int(self.get_jugador2().get_resistence()) + int(self.get_jugador2().get_resistence()) * ventaja[1]:
                    self.win_table1(self.get_jugador1(), self.get_jugador2(), gan, per)
                    return (self.get_jugador1().get_name()+ ' (' + str(gan) + ')' + ' VS ' + self.get_jugador2().get_name() +' (' + str(per) + ')')
                
                else:
                    self.win_table2(self.get_jugador1(), self.get_jugador2(), gan, per) #OPtimizar
                    return (self.get_jugador1().get_name() + ' (' + str(per) + ')' + ' VS ' + self.get_jugador2().get_name() +' (' + str(gan) + ')')
                
        if self.get_criterio() == "fuerza": #cambiar con pygame
            
            if int(self.get_jugador1().get_strength()) + int(self.get_jugador1().get_strength()) * ventaja[0] == int(self.get_jugador2().get_strength()) + int(self.get_jugador2().get_strength()) * ventaja[1]:
                if int(self.get_jugador1().get_speed()) + int(self.get_jugador1().get_speed()) * ventaja[0] == int(self.get_jugador2().get_speed()) + int(self.get_jugador2().get_speed()) * ventaja[1]:
                    self.tied_table(self.get_jugador1(), self.get_jugador2(), empate)
                    return (self.get_jugador1().get_name() + ' (' + str(empate) + ')' + ' VS ' +  self.get_jugador2().get_name() +' (' + str(empate) + ')')
                    
                else:
                    if int(self.get_jugador1().get_speed()) + int(self.get_jugador1().get_speed()) * ventaja[0] > int(self.get_jugador2().get_speed()) + int(self.get_jugador2().get_speed()) * ventaja[1]:
                        self.win_table1(self.get_jugador1(), self.get_jugador2(), gan, per) #Optimizar
            
                        return (self.get_jugador1().get_name() + ' (' + str(gan) + ')' + ' VS ' + self.get_jugador2().get_name() +' (' + str(per) + ')')
                        
                    else:
                        self.win_table2(self.get_jugador1(), self.get_jugador2(), gan, per) #OPtimizar
            
                        return (self.get_jugador1().get_name() + ' (' + str(per) + ')' + ' VS ' + self.get_jugador2().get_name() +' (' + str(gan) + ')')
                        
                
            else:
                if int(self.get_jugador1().get_strength()) + int(self.get_jugador1().get_strength()) * ventaja[0] > int(self.get_jugador2().get_strength()) + int(self.get_jugador2().get_strength()) * ventaja[1]:
                    self.win_table1(self.get_jugador1(), self.get_jugador2(), gan, per)
        
                    return (self.get_jugador1().get_name()+ ' (' + str(gan) + ')' + ' VS ' + self.get_jugador2().get_name() +' (' + str(per) + ')')
                
                else:
                    self.win_table2(self.get_jugador1(), self.get_jugador2(), gan, per) #OPtimizar
        
                    return (self.get_jugador1().get_name() + ' (' + str(per) + ')' + ' VS ' + self.get_jugador2().get_name() +' (' + str(gan) + ')')
                    
                    
        if self.get_criterio() == "velocidad": #cambiar con pygame
            if int(self.get_jugador1().get_speed()) + int(self.get_jugador1().get_speed()) * ventaja[0] == int(self.get_jugador2().get_speed()) + int(self.get_jugador2().get_speed()) * ventaja[1]:
                if int(self.get_jugador1().get_precision()) + int(self.get_jugador1().get_precision()) * ventaja[0] == int(self.get_jugador2().get_precision()) + int(self.get_jugador2().get_precision()) * ventaja[1]:
                    self.tied_table(self.get_jugador1(), self.get_jugador2(), empate)
        
                    return (self.get_jugador1().get_name() + ' (' + str(empate) + ')' + ' VS ' +  self.get_jugador2().get_name() +' (' + str(empate) + ')')
                
                else:
                    if int(self.get_jugador1().get_precision()) + int(self.get_jugador1().get_precision()) * ventaja[0] > int(self.get_jugador2().get_precision()) + int(self.get_jugador2().get_precision()) * ventaja[1]:
                        self.win_table1(self.get_jugador1(), self.get_jugador2(), gan, per) #Optimizar
            
                        return (self.get_jugador1().get_name() + ' (' + str(gan) + ')' + ' VS ' + self.get_jugador2().get_name() +' (' + str(per) + ')')
                        
                    else:
                        self.win_table2(self.get_jugador1(), self.get_jugador2(), gan, per) #OPtimizar
            
                        return (self.get_jugador1().get_name() + ' (' + str(per) + ')' + ' VS ' + self.get_jugador2().get_name() +' (' + str(gan) + ')')
                        
                
            else:
                if int(self.get_jugador1().get_speed()) + int(self.get_jugador1().get_speed()) * ventaja[0] > int(self.get_jugador2().get_speed()) + int(self.get_jugador2().get_speed()) * ventaja[1]:
                    self.win_table1(self.get_jugador1(), self.get_jugador2(), gan, per)
        
                    return (self.get_jugador1().get_name() + ' (' + str(gan) + ')' + ' VS ' + self.get_jugador2().get_name() +' (' + str(per) + ')')
                
                else:
                    self.win_table2(self.get_jugador1(), self.get_jugador2(), gan, per) #OPtimizar
        
                    return (self.get_jugador1().get_name() + ' (' + str(per) + ')' + ' VS ' + self.get_jugador2().get_name() +' (' + str(gan) + ')')
                    
                
        if self.get_criterio() == "precision": #cambiar con pygame
            if int(self.get_jugador1().get_precision()) + int(self.get_jugador1().get_precision()) * ventaja[0] == int(self.get_jugador2().get_precision()) + int(self.get_jugador2().get_precision()) * ventaja[1]:
                if int(self.get_jugador1().get_resistence()) + int(self.get_jugador1().get_resistence()) * ventaja[0] == int(self.get_jugador2().get_resistence()) + int(self.get_jugador2().get_resistence()) * ventaja[1]:
                    self.tied_table(self.get_jugador1(), self.get_jugador2(), empate)
        
                    return (self.get_jugador1().get_name() + ' (' + str(empate) + ')' + ' VS ' +  self.get_jugador2().get_name() +' (' + str(empate) + ')')
                    
                else:
                    if int(self.get_jugador1().get_resistence()) + int(self.get_jugador1().get_resistence()) * ventaja[0] > int(self.get_jugador2().get_resistence()) + int(self.get_jugador2().get_resistence()) * ventaja[1]:
                        self.win_table1(self.get_jugador1(), self.get_jugador2(), gan, per) #Optimizar
            
                        return (self.get_jugador1().get_name() + ' (' + str(gan) + ')' + ' VS ' + self.get_jugador2().get_name() +' (' + str(per) + ')')
                        
                    else:
                        self.win_table2(self.get_jugador1(), self.get_jugador2(), gan, per) #OPtimizar
            
                        return (self.get_jugador1().get_name() + ' (' + str(per) + ')' + ' VS ' + self.get_jugador2().get_name() +' (' + str(gan) + ')')
                    
            else:
                if int(self.get_jugador1().get_precision()) + int(self.get_jugador1().get_precision()) * ventaja[0] > int(self.get_jugador2().get_precision()) + int(self.get_jugador2().get_precision()) * ventaja[1]:
                    self.win_table1(self.get_jugador1(), self.get_jugador2(), gan, per)
        
                    return (self.get_jugador1().get_name()+ ' (' + str(gan) + ')' + ' VS ' + self.get_jugador2().get_name() +' (' + str(per) + ')')
                    
                else:
                    self.win_table2(self.get_jugador1(), self.get_jugador2(), gan, per) #OPtimizar
        
                    return (self.get_jugador1().get_name() + ' (' + str(per) + ')' + ' VS ' + self.get_jugador2().get_name() +' (' + str(gan) + ')')
                    
     def assign_winner2(self):
        gan = self.ganador(5)
        per = self.ganador(gan-1)
        empate = self.empate()
        ventaja = self.ventaja_terreno()
        if gan-per == 2:
            ganpor2= 1
        else:
            ganpor2=0
        #revisar
        if self.get_criterio() == "resistencia": #cambiar con pygame
            if self.get_jugador1().get_resistence() + self.get_jugador1().get_resistence() * ventaja[0] == self.get_jugador2().get_resistence() + self.get_jugador2().get_resistence() * ventaja[1]:
                
                if self.get_jugador1().get_strength() + self.get_jugador1().get_strength() * ventaja[0] == self.get_jugador2().get_strength() + self.get_jugador2().get_strength() * ventaja[1]:
                    
                    self.tied_table(self.get_jugador1(), self.get_jugador2(), empate)
                    if not self.goles_contados:
                        Partido.goles_totales += empate*2
                        self.goles_contados = True
                    print("Llegue aqui 1")
                    return (self.get_jugador1(),(self.get_jugador1().get_name() + ' (' + str(empate) + ')' + ' VS ' +  self.get_jugador2().get_name() +' (' + str(empate) + ')'))

                    
                else:
                    if self.get_jugador1().get_strength() + self.get_jugador1().get_strength() * ventaja[0] > self.get_jugador2().get_strength() + self.get_jugador2().get_strength()* ventaja[1]:
                        self.win_table1(self.get_jugador1(), self.get_jugador2(), gan, per) #Optimizar
                        if not self.goles_contados:
                            Partido.goles_totales += gan + per
                            self.goles_contados = True
                        print("Llegue aqui 2")
                        return (self.get_jugador1(),(self.get_jugador1().get_name() + ' (' + str(gan) + ')' + ' VS ' + self.get_jugador2().get_name() +' (' + str(per) + ')'))
                        
                    else:
                        self.win_table2(self.get_jugador1(), self.get_jugador2(), gan, per) #OPtimizar
                        if not self.goles_contados:
                            Partido.goles_totales += gan + per
                            self.goles_contados = True
                        print("Llegue aqui 3")
                        return (self.get_jugador2(),(self.get_jugador1().get_name() + ' (' + str(per) + ')' + ' VS ' + self.get_jugador2().get_name() +' (' + str(gan) + ')'))
                        
                
            else:
            
                if self.get_jugador1().get_resistence() + self.get_jugador1().get_resistence() * ventaja[0] > self.get_jugador2().get_resistence() + self.get_jugador2().get_resistence() * ventaja[1]:
                    self.win_table1(self.get_jugador1(), self.get_jugador2(), gan, per)
                    if not self.goles_contados:
                        Partido.goles_totales += gan + per
                        self.goles_contados = True
                    return (self.get_jugador1(), (self.get_jugador1().get_name()+ ' (' + str(gan) + ')' + ' VS ' + self.get_jugador2().get_name() +' (' + str(per) + ')'))
                
                else:
                    self.win_table2(self.get_jugador1(), self.get_jugador2(), gan, per) #OPtimiza
                    if not self.goles_contados:
                        Partido.goles_totales += gan + per
                        self.goles_contados = True
                    return (self.get_jugador2(),(self.get_jugador1().get_name() + ' (' + str(per) + ')' + ' VS ' + self.get_jugador2().get_name() +' (' + str(gan) + ')'))
                
        if self.get_criterio() == "fuerza": #cambiar con pygame
            
            if self.get_jugador1().get_strength() + self.get_jugador1().get_strength() * ventaja[0] == self.get_jugador2().get_strength() + self.get_jugador2().get_strength() * ventaja[1]:
                if self.get_jugador1().get_speed() + self.get_jugador1().get_speed() * ventaja[0] == self.get_jugador2().get_speed() + self.get_jugador2().get_speed() * ventaja[1]:
                    self.tied_table(self.get_jugador1(), self.get_jugador2(), empate)
                    if not self.goles_contados:
                        Partido.goles_totales += empate*2
                        self.goles_contados = True
                    return (self.get_jugador1(),(self.get_jugador1().get_name() + ' (' + str(empate) + ')' + ' VS ' +  self.get_jugador2().get_name() +' (' + str(empate) + ')'))
                    
                else:
                    if self.get_jugador1().get_speed() + self.get_jugador1().get_speed() * ventaja[0] > self.get_jugador2().get_speed() + self.get_jugador2().get_speed()* ventaja[1]:
                        self.win_table1(self.get_jugador1(), self.get_jugador2(), gan, per) #Optimizar
                        if not self.goles_contados:
                            Partido.goles_totales += gan + per
                            self.goles_contados = True
                        return (self.get_jugador1(),(self.get_jugador1().get_name() + ' (' + str(gan) + ')' + ' VS ' + self.get_jugador2().get_name() +' (' + str(per) + ')'))
                        
                    else:
                        self.win_table2(self.get_jugador1(), self.get_jugador2(), gan, per) #OPtimizar
                        if not self.goles_contados:
                            Partido.goles_totales += gan + per
                            self.goles_contados = True
                        return (self.get_jugador2(),(self.get_jugador1().get_name() + ' (' + str(per) + ')' + ' VS ' + self.get_jugador2().get_name() +' (' + str(gan) + ')'))
                        
                
            else:
                if self.get_jugador1().get_strength()+ self.get_jugador1().get_strength() * ventaja[0] > self.get_jugador2().get_strength() + self.get_jugador2().get_strength() * ventaja[1]:
                    self.win_table1(self.get_jugador1(), self.get_jugador2(), gan, per)
                    if not self.goles_contados:
                        Partido.goles_totales += gan + per
                        self.goles_contados = True
                    return (self.get_jugador1(),(self.get_jugador1().get_name()+ ' (' + str(gan) + ')' + ' VS ' + self.get_jugador2().get_name() +' (' + str(per) + ')'))
                
                else:
                    self.win_table2(self.get_jugador1(), self.get_jugador2(), gan, per) #OPtimiza
                    if not self.goles_contados:
                        Partido.goles_totales += gan + per
                        self.goles_contados = True
                    return (self.get_jugador2(),(self.get_jugador1().get_name() + ' (' + str(per) + ')' + ' VS ' + self.get_jugador2().get_name() +' (' + str(gan) + ')'))
                    
                    
        if self.get_criterio() == "velocidad": #cambiar con pygame
            if self.get_jugador1().get_speed() + self.get_jugador1().get_speed() * ventaja[0] == self.get_jugador2().get_speed() + self.get_jugador2().get_speed() * ventaja[1]:
                if self.get_jugador1().get_precision() + self.get_jugador1().get_precision() * ventaja[0] == self.get_jugador2().get_precision() + self.get_jugador2().get_precision() * ventaja[1]:
                    self.tied_table(self.get_jugador1(), self.get_jugador2(), empate)
                    if not self.goles_contados:
                        Partido.goles_totales += empate*2
                        self.goles_contados = True
                    return (self.get_jugador1(),(self.get_jugador1().get_name() + ' (' + str(empate) + ')' + ' VS ' +  self.get_jugador2().get_name() +' (' + str(empate) + ')'))
                
                else:
                    if self.get_jugador1().get_precision() + self.get_jugador1().get_precision() * ventaja[0] > self.get_jugador2().get_precision() + self.get_jugador2().get_precision() * ventaja[1]:
                        self.win_table1(self.get_jugador1(), self.get_jugador2(), gan, per) #Optimizar
                        if not self.goles_contados:
                            Partido.goles_totales += gan + per
                            self.goles_contados = True
                        return (self.get_jugador1(),(self.get_jugador1().get_name() + ' (' + str(gan) + ')' + ' VS ' + self.get_jugador2().get_name() +' (' + str(per) + ')'))
                        
                    else:
                        self.win_table2(self.get_jugador1(), self.get_jugador2(), gan, per) #OPtimizar
                        if not self.goles_contados:
                            Partido.goles_totales += gan + per
                            self.goles_contados = True
                        return (self.get_jugador2(),(self.get_jugador1().get_name() + ' (' + str(per) + ')' + ' VS ' + self.get_jugador2().get_name() +' (' + str(gan) + ')'))
                        
                
            else:
                if self.get_jugador1().get_speed()+ self.get_jugador1().get_speed() * ventaja[0] > self.get_jugador2().get_speed() + self.get_jugador2().get_speed() * ventaja[1]:
                    self.win_table1(self.get_jugador1(), self.get_jugador2(), gan, per)
                    if not self.goles_contados:
                        Partido.goles_totales += gan + per
                        self.goles_contados = True
                    return (self.get_jugador1(),(self.get_jugador1().get_name() + ' (' + str(gan) + ')' + ' VS ' + self.get_jugador2().get_name() +' (' + str(per) + ')'))
                
                else:
                    self.win_table2(self.get_jugador1(), self.get_jugador2(), gan, per) #OPtimiza
                    if not self.goles_contados:
                        Partido.goles_totales += gan + per
                        self.goles_contados = True
                    return (self.get_jugador2(),(self.get_jugador1().get_name() + ' (' + str(per) + ')' + ' VS ' + self.get_jugador2().get_name() +' (' + str(gan) + ')'))
                    
                
        if self.get_criterio() == "presicion": #cambiar con pygame
            
            if self.get_jugador1().get_precision() + self.get_jugador1().get_precision() * ventaja[0] == self.get_jugador2().get_precision()+ self.get_jugador2().get_precision() * ventaja[1]:
                if self.get_jugador1().get_resistence() + self.get_jugador1().get_resistence() * ventaja[0] == self.get_jugador2().get_resistence() + self.get_jugador2().get_resistence() * ventaja[1]:
                    self.tied_table(self.get_jugador1(), self.get_jugador2(), empate)
                    if not self.goles_contados:
                        Partido.goles_totales += empate*2
                        self.goles_contados = True
                    return (self.get_jugador1(),(self.get_jugador1().get_name() + ' (' + str(empate) + ')' + ' VS ' +  self.get_jugador2().get_name() +' (' + str(empate) + ')'))
                    
                else:
                    if self.get_jugador1().get_resistence() + self.get_jugador1().get_resistence() * ventaja[0] > self.get_jugador2().get_resistence() + self.get_jugador2().get_resistence() * ventaja[1]:
                        self.win_table1(self.get_jugador1(), self.get_jugador2(), gan, per) #Optimizar
                        if not self.goles_contados:
                            Partido.goles_totales += gan + per
                            self.goles_contados = True
                        return (self.get_jugador1(),(self.get_jugador1().get_name() + ' (' + str(gan) + ')' + ' VS ' + self.get_jugador2().get_name() +' (' + str(per) + ')'))
                        
                    else:
                        self.win_table2(self.get_jugador1(), self.get_jugador2(), gan, per) #OPtimizar        
                        if not self.goles_contados:
                            Partido.goles_totales += gan + per
                            self.goles_contados = True
                        return (self.get_jugador2(),(self.get_jugador1().get_name() + ' (' + str(per) + ')' + ' VS ' + self.get_jugador2().get_name() +' (' + str(gan) + ')'))
                    
            else:
                if self.get_jugador1().get_precision()+ self.get_jugador1().get_precision() * ventaja[0] > self.get_jugador2().get_precision() + self.get_jugador2().get_precision() * ventaja[1]:
                    self.win_table1(self.get_jugador1(), self.get_jugador2(), gan, per)
                    if not self.goles_contados:
                        Partido.goles_totales += gan + per
                        self.goles_contados = True
                    return (self.get_jugador1(),(self.get_jugador1().get_name()+ ' (' + str(gan) + ')' + ' VS ' + self.get_jugador2().get_name() +' (' + str(per) + ')'))
                    
                else:
                    self.win_table2(self.get_jugador1(), self.get_jugador2(), gan, per) #OPtimiza
                    if not self.goles_contados:
                        Partido.goles_totales += gan + per
                        self.goles_contados = True
                    return (self.get_jugador2(),(self.get_jugador1().get_name() + ' (' + str(per) + ')' + ' VS ' + self.get_jugador2().get_name() +' (' + str(gan) + ')'))

        