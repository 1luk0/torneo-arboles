import random

class Teams:
    def __init__(self, name, group, resintence, strength, speed, precision, descalificado,bandera,costumbre_terreno, games_played, games_won, games_tied, games_losed, goals_favor, goals_against, points,players):
        self.__name = name
        self.__group = group
        self.__resintence = resintence
        self.__strength = strength
        self.__speed = speed
        self.__precision = precision
        self.__descalificado = descalificado
        self.__bandera = bandera
        self.__costumbre_terreno = costumbre_terreno
        self.__games_played = games_played
        self.__games_won = games_won
        self.__games_tied = games_tied
        self.__games_losed = games_losed
        self.__goals_favor = goals_favor
        self.__goals_against = goals_against
        self.__points = points
        self.__players = players
        self.__dinero=0
        self.__ganaPor2=0
    

    # Getters
    def get_name(self):
        return self.__name

    def get_group(self):
        return self.__group

    def get_resistence(self):
        return self.__resintence

    def get_strength(self):
        return self.__strength

    def get_speed(self):
        return self.__speed

    def get_descalificado(self):
        return self.__descalificado
    
    def get_precision(self):
        if self.__precision == "Alto":
            return 3
        elif self.__precision== "Medio":
            return 2 
        elif self.__precision=="Bajo":
            return 1
    
    def get_bandera(self):
        return self.__bandera
    
    def get_costumbre_terreno(self):
        if self.__costumbre_terreno =="Alto":
            return 1 
        elif self.__costumbre_terreno =="Medio":
            return 2
        elif self.__costumbre_terreno =="Bajo":
            return 3

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
    
    def get_players(self):
        return self.__players
    
    def get_dinero(self):
        return self.__dinero
    
    def get_ganaPor2(self):
        return self.__ganaPor2

    # Setters
    def set_name(self, name):
        self.__name = name

    def set_group(self, group): #La lista de grupos se inicializa todos en none
        self.__group = group

    def set_resistence(self, resistence):
        self.__resintence = int(resistence)

    def set_strength(self, strength):
        self.__strength = strength
    
    def set_speed(self, speed):
        self.__speed = speed
    
    def set_precision(self,precision):
        if precision == "Alto":
            self.__precision= 3
        elif precision == "Medio":
            self.__precision= 2
        elif precision =="Bajo":
            self.__precision= 1
        elif precision == "Descalificado":
            self.__precision = -1

    def set_bandera(self, band):
        self.__bandera = band

    def set_costrumbre_terreno(self, costumbre_terreno):
        if costumbre_terreno =="Alto":
            self.__costumbre_terreno = 1
        elif costumbre_terreno =="Medio":
            self.__costumbre_terreno = 2
        elif costumbre_terreno =="Bajo":
            self.__costumbre_terreno == 3
    
    def set_games_won(self, games_won):
        self.__games_won = games_won
        
    def set_games_played(self,games_played):
        self.__games_played = games_played
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

    def set_player(self,players):
        self.__players = players

    def set_dinero(self,dinero):
        self.__dinero= dinero

    def set_ganaPor2(self,ganapor2):
        self.__ganaPor2= ganapor2