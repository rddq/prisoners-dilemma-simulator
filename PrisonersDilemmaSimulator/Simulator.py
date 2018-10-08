from Game import Game
from Player import Player
from AnalysisHelper import AnalysisHelper

import numpy

class Simulator:
    
    def __init__(self):
        pass
    
if __name__ == '__main__':
    
    all_results = []
    data_for_csv = []
    for i in range(0,9):
        players = [Player(player_type=0,player_number=0),Player(player_type=i,player_number=1)]   
        game = Game(players)
        results_5 = game.playGame(5)
        AnalysisHelper.add_to_csv(data_for_csv,results_5,game,i)
        results_100 = game.playGame(100)
        AnalysisHelper.add_to_csv(data_for_csv,results_100,game,i)
        results_200 = game.playGame(200)
        AnalysisHelper.add_to_csv(data_for_csv,results_200,game,i)
        for j in range(0,30):
            results_p75 = game.playGame(10000, 0.75)
            AnalysisHelper.add_to_csv(data_for_csv,results_p75,game,i)
            results_p90 = game.playGame(10000, 0.9)
            AnalysisHelper.add_to_csv(data_for_csv,results_p90,game,i)
            results_p99 = game.playGame(10000, 0.99)
            AnalysisHelper.add_to_csv(data_for_csv,results_p99,game,i)
    data = numpy.asarray(data_for_csv)
    numpy.savetxt("PrisonersDilemmaMatchData.csv", data, delimiter=",")
        
        
    

