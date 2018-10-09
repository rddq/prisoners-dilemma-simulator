from Game import Game
from Player import Player
from AnalysisHelper import AnalysisHelper

import pandas

class Simulator:
    
    def __init__(self):
        pass
    
if __name__ == '__main__':   
    names_of_strategies = {
        0 : "Two tits for a tat",
        1 : "Always defect",
        2 : "Random",
        3 : "Always Cooperate",
        4 : "Tit for a tat",
        5 : "Tit for two tats",
        6 : "Pavlov strategy",
        7 : "Win stay lose shift",
        8 : "Never forgive"
    }

    all_results = []
    data_for_csv = []
    for player_1_type in range(0,9):
        for player_2_type in range(0,9):
            players = [Player(player_1_type,player_number=0),Player(player_2_type,player_number=1)]   
            game = Game(players)
            results_5 = game.playGame(5)
            player_1_strat = names_of_strategies.get(player_1_type)
            player_2_strat = names_of_strategies.get(player_2_type)

            AnalysisHelper.add_to_csv(data_for_csv,results_5,game,player_1_strat,player_2_strat,"5 games")
            
            results_100 = game.playGame(100)
            AnalysisHelper.add_to_csv(data_for_csv,results_100,game,player_1_strat,player_2_strat,"100 games")
            
            results_200 = game.playGame(200)
            AnalysisHelper.add_to_csv(data_for_csv,results_200,game,player_1_strat,player_2_strat, "200 games")
            for k in range(0,30):
                results_p75 = game.playGame(10000, 0.75)
                AnalysisHelper.add_to_csv(data_for_csv,results_p75,game,player_1_strat,player_2_strat, "Beta = 0.75")
                
                results_p90 = game.playGame(10000, 0.9)
                AnalysisHelper.add_to_csv(data_for_csv,results_p90,game,player_1_strat,player_2_strat, "Beta = 0.9")
                
                results_p99 = game.playGame(10000, 0.99)
                AnalysisHelper.add_to_csv(data_for_csv,results_p99,game,player_1_strat,player_2_strat, "Beta = 0.99")
    labels = ["Player 1", "Player 2", "Number of Rounds", "Game Type", "Player 1 Score", "Player 2 Score"]
    data = pandas.DataFrame.from_records(data_for_csv, columns=labels)
    data.to_csv("PrisonersDilemmaMatchData.csv",  sep=",")        