from Game import Game
from Player import Player
from PlotHelper import PlotHelper

class Simulator:
    
    def __init__(self):
        pass
    
if __name__ == '__main__':
    players = [Player(player_type=2,player_number=0),Player(player_type=6,player_number=1)]
    game = Game(players, 0.98)
    results = game.playGame(500)
    PlotHelper().plot_player_rewards_over_time(results)