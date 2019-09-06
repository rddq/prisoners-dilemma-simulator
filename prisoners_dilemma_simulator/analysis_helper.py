import matplotlib.pyplot as plt
import numpy as np

class AnalysisHelper:
    def __init__(self):
        pass

    @staticmethod
    def total_score(results):
        results = np.array(results)
        return [(sum(results[:, -2])), (sum(results[:, -1])), ]

    @staticmethod
    def run_analysis_all_matchups(match_results):
        i = 1
        for match_result in match_results:
            print("You Against Player "+str(i))
            AnalysisHelper.run_analysis_all_games(match_result)
            i += 1

    @staticmethod
    def run_analysis_all_games(match_result):
        for game_result in match_result:
            AnalysisHelper.run_analysis_on_game(game_result)

    @staticmethod
    def run_analysis_on_game(game_result):
        score_totals = AnalysisHelper.total_score(game_result)
        if (score_totals[0] == score_totals[1]):
            print("Tie")
        else:
            winner = score_totals.index(max(score_totals))
            print("Winner: Player " + str(winner))
        print(score_totals)
