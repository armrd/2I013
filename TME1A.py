from soccersimulator  import Strategy, SoccerAction, Vector2D
from soccersimulator import SoccerTeam, Simulation
from soccersimulator import show_simu


## Strategie aleatoire
class RandomStrategy(Strategy):
    def __init__(self):
        Strategy.__init__(self,"Random")
    def compute_strategy(self,state,id_team,id_player):
        return SoccerAction(Vector2D.create_random(-0.5,0.5),Vector2D.create_random(-1,1))

#class FonceurStrategy(Strategy):
 #   def __init__(self):
  #      Strategy.__init__(self,"Random")
   # def compute_strategy(self,state,id_team,id_player):
    #    return SoccerAction(,)

    
## Creation d'une equipe
pyteam = SoccerTeam(name="PyTeam")
thon = SoccerTeam(name="ThonTeam")
pyteam.add("PyPlayer",RandomStrategy()) #Strategie qui ne fait rien
thon.add("ThonPlayer",RandomStrategy())   #Strategie aleatoire

vitesse=state.ball.position


#Creation d'une partie
simu = Simulation(pyteam,thon)
#Jouer et afficher la partie
show_simu(simu)


