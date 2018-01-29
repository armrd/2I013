from soccersimulator import Strategy, SoccerAction, Vector2D
from soccersimulator import SoccerTeam, Simulation
from soccersimulator import show_simu
import math

## Strategie aleatoire
class RandomStrategy(Strategy):
    def __init__(self):
        Strategy.__init__(self,"Random")
    def compute_strategy(self,state,id_team,id_player):
        return SoccerAction(Vector2D.create_random(-0.5,0.5),Vector2D.create_random(-1,1))

class Balle:
    bpos=state.ball.position #position de la balle
    vball=state.ball.vitesse #vitesse de la balle
    
class Fonceur(Strategy):
    
    vitesse=Vector2D(2,0)
    shoot=Vector2D(1,0)
    
    def __init__(self):
        Strategy.__init__(self,"Foncer")
    def compute_strategy(self,state,id_team,id_player):
        if(abs(state.player_state(1,0).position.x-state.ball.position.x)<.35 and abs(state.player_state(1,0).position.y-state.ball.position.y)<.35 ):
            return SoccerAction(Vector2D(0,0))
        return SoccerAction(vitesse)
        

    
## Creation d'une equipe
pyteam = SoccerTeam(name="PyTeam")
thon = SoccerTeam(name="ThonTeam")
pyteam.add("PyPlayer",Fonceur()) #Strategie qui ne fait rien
thon.add("ThonPlayer",RandomStrategy())   #Strategie aleatoire

#balle=ball.position
#print (balle)
#act1 = SoccerAction(vitesse,shoot)
#act2 = SoccerAction(vitesse,shoot)

#act_new=act1+act2

#Creation d'une partie
simu = Simulation(pyteam,thon)
#Jouer et afficher la partie
show_simu(simu)



