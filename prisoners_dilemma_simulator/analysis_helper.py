import matplotlib.pyplot as plt
import numpy as np


class PlotHelper:

    def __init__(self):
        pass

    @staticmethod
    def _results_over_time__(player_results):
        results_over_time = [sum(player_results[0:i])
                             for i in range(0, len(player_results))]
        return results_over_time

    @staticmethod
    def plot_player_rewards_over_time(results):
        results = np.array(results)
        p1_results = results[:, -2]
        p1_summation = PlotHelper._results_over_time__(p1_results)
        p2_results = results[:, -1]
        p2_summation = PlotHelper._results_over_time__(p2_results)

        _, ax1 = plt.subplots()

        x = range(0, len(results))
        ax1.plot(x, p1_summation, label="Player 1 Reward", color='r')
        ax1.plot(x, p2_summation, label="Player 2 Reward", color='g')

        ax1.set_xlim(0, len(results))
        ax1.set_title('Cumulative Reward vs Round Number')

        ax1.set_xlabel('Round Number')
        ax1.set_ylabel('Reward')

        ax1.grid()
        ax1.legend()

        plt.show()
        print("plot")
        # If it looks like there is only one line showing up,
        # they are on top of each other


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
