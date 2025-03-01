import random

class Teams:
    def __init__(self, name, group, resistence, strength, speed, precisionA, precisionM, precisionB, games_played, games_won, games_tied, games_losed, goals_favor, goals_against, points):
        self.__name = name
        self.__group = group
        self.__resistence = resistence
        self.__strength = strength
        self.__speed = speed
        self.__precisionA = precisionA
        self.__precisionM = precisionM
        self.__precisionB = precisionB
        self.__games_played = games_played
        self.__games_won = games_won
        self.__games_tied = games_tied
        self.__games_losed = games_losed
        self.__goals_favor = goals_favor
        self.__goals_against = goals_against
        self.__points = points

    # Getters
    def get_name(self):
        return self.__name

    def get_group(self):
        return self.__group

    def get_resistence(self):
        return self.__resistence

    def get_strength(self):
        return self.__strength

    def get_speed(self):
        return self.__speed

    def get_precisionA(self):
        return self.__precisionA

    def get_precisionM(self):
        return self.__precisionM

    def get_precisionB(self):
        return self.__precisionB

    def get_games_played(self):
        return self.__games_played

    def get_games_won(self):
        return self.__games_won

    def get_games_tied(self):
        return self.__games_tied

    def get_games_losed(self):
        return self.__games_losed

    def get_goals_favor(self):
        return self.__goals_favor

    def get_goals_against(self):
        return self.__goals_against

    def get_points(self):
        return self.__points

    # Setters
    def set_name(self, name):
        self.__name = name

    def set_group(self, group): #La lista de grupos se inicializa todos en none
        for i in group:
            if i is None:    
                self.__group = group
                return 
        print('el equipo no se puede agregar a este grupo ya que este está lleno, escoja otro')
                

    def set_resistence(self, resistence):
        self.__resistence = resistence

    def set_strength(self, strength):
        self.__strength = strength

    def set_speed(self, speed):
        self.__speed = speed

    def set_precisionA(self, precisionA):
        self.__precisionA = precisionA

    def set_precisionM(self, precisionM):
        self.__precisionM = precisionM

    def set_precisionB(self, precisionB):
        self.__precisionB = precisionB

    def set_games_played(self, games_played):
        self.__games_played = games_played

    def set_games_won(self, games_won):
        self.__games_won = games_won

    def set_games_tied(self, games_tied):
        self.__games_tied = games_tied

    def set_games_losed(self, games_losed):
        self.__games_losed = games_losed

    def set_goals_favor(self, goals_favor):
        self.__goals_favor = goals_favor

    def set_goals_against(self, goals_against):
        self.__goals_against = goals_against

    def set_points(self, points):
        self.__points = points

class Tournament:
    
    def __init__(self,criterion,stadium):
        self.__criterion = criterion
        self.__stadium = stadium
        
    def empate(self, team1,team2):
        emp = random.randint(0, 3)
        return emp
    
    def ganador(self,team1,tema2,g):
        if g > 0:
            gan = random.randint(1, g)
            return gan
        else:
            return 0
    
    def tied_table(self,team1,team2,emp):
        team1.points += 1
        team2.points += 1
        team1.games_tied += 1
        team2.games_tied += 1
        team1.goals_against += emp
        team1.goals_favor += emp
        team2.goals_against += emp
        team2.goals_favor += emp
        team1.games_played += 1
        team2.games_played += 1
    
    def win_table1(self,team1,team2,gan,per):
        team1.games_played += 1
        team2.games_played += 1
        team1.points += 3
        team1.games_won += 1
        team2.games_losed += 1
        team1.goals_against = per
        team1.goals_favor = gan
        team2.goals_against = gan
        team2.goals_favor = per
    
    def win_table2(self,team1,team2,gan,per):
        team1.games_played += 1
        team2.games_played += 1
        team2.points += 3
        team2.games_won += 1
        team1.games_losed += 1
        team2.goals_against = per
        team2.goals_favor = gan
        team1.goals_against = gan
        team1.goals_favor = per
    
    def assign_winner(self,team1,team2,criterion,stadium): #Se deben cambiar los condicionales para que estos sean las opciones marcadas en el pygame y los returns 
        gan = self.ganador(team1, team2,5)
        per = self.ganador(team1, team2,gan-1)
        empate = self.empate(team1, team2)
        #revisar
        if criterion == "resistencia": #cambiar con pygame
            if team1.resistence == team2.resistence:
                if team1.strength == team2.strength:
                    print(team1.name+ ' (' + empate + ')' + ' VS ' + team2.name +' (' + empate + ')')
                    self.tied_table(team1, team2, empate)
                else:
                    
                    if team1.strength > team2.strength:
                        print(team1.name+ ' (' + gan + ')' + ' VS ' + team2.name +' (' + per + ')')
                        self.win_table1(team1, team2, gan, per) #Optimizar
                    else:
                        print(team1.name+ ' (' + per + ')' + ' VS ' + team2.name +' (' + gan + ')')
                        self.win_table2(team1, team2, gan, per) #OPtimizar
            else:
                if team1.resistence > team2.resistence:
                    print(team1.name+ ' (' + gan + ')' + ' VS ' + team2.name +' (' + per + ')')
                    self.win_table1(team1, team2, gan, per) 
                else:
                    print(team1.name+ ' (' + per + ')' + ' VS ' + team2.name +' (' + gan + ')')
                    self.win_table2(team1, team2, gan, per)
                
        if criterion == "fuerza": #cambiar con pygame
            if team1.strength == team2.strength:
                if team1.speed == team2.speed:
                    print(team1.name+ ' (' + empate + ')' + ' VS ' + team2.name +' (' + empate + ')')
                    self.tied_table(team1, team2, empate)
                   
                else:
                    if team1.speed > team2.speed:
                        print(team1.name+ ' (' + gan + ')' + ' VS ' + team2.name +' (' + per + ')')
                        self.win_table1(team1, team2, gan, per)
                      
                    else:
                        print(team1.name+ ' (' + per + ')' + ' VS ' + team2.name +' (' + gan + ')')
                        self.win_table2(team1, team2, gan, per)
            else:
                if team1.strength > team2.strength:
                    print(team1.name+ ' (' + gan + ')' + ' VS ' + team2.name +' (' + per + ')')
                    self.win_table1(team1, team2, gan, per)
                 
                else:
                    print(team1.name+ ' (' + per + ')' + ' VS ' + team2.name +' (' + gan + ')')
                    self.win_table2(team1, team2, gan, per)
        
        if criterion == "velocidad": #cambiar con pygame
            if team1.speed == team2.speed:
                if stadium == 'alto':
                    if team1.precisionA == team2.precisionA:
                        print(team1.name+ ' (' + empate + ')' + ' VS ' + team2.name +' (' + empate + ')')
                        self.tied_table(team1, team2, empate)
                       
                    else:
                        if team1.precisionA > team2.precisionA:
                            print(team1.name+ ' (' + gan + ')' + ' VS ' + team2.name +' (' + per + ')')
                            self.win_table1(team1, team2, gan, per)
                        
                        else:
                            print(team1.name+ ' (' + per + ')' + ' VS ' + team2.name +' (' + gan + ')')
                            self.win_table2(team1, team2, gan, per)
                if stadium == 'medio':
                    if team1.precisionM == team2.precisionM:
                        print(team1.name+ ' (' + empate + ')' + ' VS ' + team2.name +' (' + empate + ')')
                        self.tied_table(team1, team2, empate)
                     
                    else:
                        if team1.precisionM > team2.precisionM:
                            print(team1.name+ ' (' + gan + ')' + ' VS ' + team2.name +' (' + per + ')')
                            self.win_table1(team1, team2, gan, per)
                          
                        else:
                            print(team1.name+ ' (' + per + ')' + ' VS ' + team2.name +' (' + gan + ')')
                            self.win_table2(team1, team2, gan, per)
                if stadium == 'bajo':
                    if team1.precisionB == team2.precisionB:
                        print(team1.name+ ' (' + empate + ')' + ' VS ' + team2.name +' (' + empate + ')')
                        self.tied_table(team1, team2, empate)
                      
                    else:
                        if team1.precisionB > team2.precisionB:
                            print(team1.name+ ' (' + gan + ')' + ' VS ' + team2.name +' (' + per + ')')
                            self.win_table1(team1, team2, gan, per)
                            
                        else:
                            print(team1.name+ ' (' + per + ')' + ' VS ' + team2.name +' (' + gan + ')')
                            self.win_table2(team1, team2, gan, per)
            else:
                if team1.strength > team2.strength:
                    print(team1.name+ ' (' + gan + ')' + ' VS ' + team2.name +' (' + per + ')')
                    self.win_table1(team1, team2, gan, per)
                    
                else:
                    print(team1.name+ ' (' + per + ')' + ' VS ' + team2.name +' (' + gan + ')')
                    self.win_table2(team1, team2, gan, per)
                
        if criterion == "precision": #cambiar con pygame
                if stadium == 'alto':
                    if team1.precisionA == team2.precisionA:
                        if team1.resistence == team2.resistence:
                            print(team1.name+ ' (' + empate + ')' + ' VS ' + team2.name +' (' + empate + ')')
                            self.tied_table(team1, team2, empate)
                      
                        else:
                            if team1.resistence > team2.resistence:
                                print(team1.name+ ' (' + gan + ')' + ' VS ' + team2.name +' (' + per + ')')
                                self.win_table1(team1, team2, gan, per)
                                
                            else:
                                print(team1.name+ ' (' + per + ')' + ' VS ' + team2.name +' (' + gan + ')')
                                self.win_table2(team1, team2, gan, per)
                    else:
                        if team1.precisionA > team2.precisionA:
                            print(team1.name+ ' (' + gan + ')' + ' VS ' + team2.name +' (' + per + ')')
                            self.win_table1(team1, team2, gan, per)
                            
                        else:
                            print(team1.name+ ' (' + per + ')' + ' VS ' + team2.name +' (' + gan + ')')
                            self.win_table2(team1, team2, gan, per)
                if stadium == 'medio':
                    if team1.precisionM == team2.precisionM:
                        if team1.resistence == team2.resistence:
                            print(team1.name+ ' (' + empate + ')' + ' VS ' + team2.name +' (' + empate + ')')
                            self.tied_table(team1, team2, empate)
                       
                        else:
                            if team1.resistence > team2.resistence:
                                print(team1.name+ ' (' + gan + ')' + ' VS ' + team2.name +' (' + per + ')')
                                self.win_table1(team1, team2, gan, per)
                               
                            else:
                                print(team1.name+ ' (' + per + ')' + ' VS ' + team2.name +' (' + gan + ')')
                                self.win_table2(team1, team2, gan, per)
                    else:
                        if team1.precisionM > team2.precisionM:
                            print(team1.name+ ' (' + gan + ')' + ' VS ' + team2.name +' (' + per + ')')
                            self.win_table1(team1, team2, gan, per)
                            
                        else:
                            print(team1.name+ ' (' + per + ')' + ' VS ' + team2.name +' (' + gan + ')')
                            self.win_table2(team1, team2, gan, per)
                if stadium == 'bajo':
                    if team1.precisionB == team2.precisionB:
                        if team1.resistence == team2.resistence:
                            print(team1.name+ ' (' + empate + ')' + ' VS ' + team2.name +' (' + empate + ')')
                            self.tied_table(team1, team2, empate)
                            
                        else:
                            if team1.resistence > team2.resistence:
                                print(team1.name+ ' (' + gan + ')' + ' VS ' + team2.name +' (' + per + ')')
                                self.win_table1(team1, team2, gan, per)
                                
                            else:
                                print(team1.name+ ' (' + per + ')' + ' VS ' + team2.name +' (' + gan + ')')
                                self.win_table2(team1, team2, gan, per)
                    else:
                        if team1.precisionB > team2.precisionB:
                            print(team1.name+ ' (' + gan + ')' + ' VS ' + team2.name +' (' + per + ')')
                            self.win_table1(team1, team2, gan, per)
                            
                        else:
                            print(team1.name+ ' (' + per + ')' + ' VS ' + team2.name +' (' + gan + ')')
                            self.win_table2(team1, team2, gan, per)
           
