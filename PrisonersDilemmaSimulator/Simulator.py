from Game import Game
from Player import Player
from AnalysisHelper import AnalysisHelper

class Simulator:
    
    def __init__(self):
        pass
    
if __name__ == '__main__':
    
    all_results = []
    for i in range(0,8):
        players = [Player(player_type=0,player_number=0),Player(player_type=i,player_number=1)]   
        game = Game(players)
        results_5 = game.playGame(5)
        results_100 = game.playGame(100)
        results_200 = game.playGame(200)
        results_p75 = game.playGame(10000, 0.75)
        results_p90 = game.playGame(10000, 0.9)
        results_p99 = game.playGame(10000, 0.99)
        results_for_our_strategy_vs_type_i = [results_5, results_100, results_200, results_p75, results_p90, results_p99]
        all_results.append(results_for_our_strategy_vs_type_i)        
    AnalysisHelper.run_analysis_all_matchups(all_results)
        
        
