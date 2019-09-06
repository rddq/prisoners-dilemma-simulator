import pandas

from prisoners_dilemma_simulator.game import Game
from prisoners_dilemma_simulator.player import Player
from prisoners_dilemma_simulator.analysis_helper import AnalysisHelper, PlotHelper


class Simulator:
    def __init__(self):
        self.names_of_strategies = {
            0: "Two tits for a tat",
            1: "Always defect",
            2: "Random",
            3: "Always Cooperate",
            4: "Tit for a tat",
            5: "Tit for two tats",
            6: "Pavlov strategy",
            7: "Win stay lose shift",
            8: "Never forgive"
        }
        self.game_type = {
            0: "5 rounds",
            1: "100 rounds",
            2: "200 rounds",
            3: "Beta = 0.9",
            4: "Beta = 0.95",
            5: "Beta = 0.99",
        }

    def simulate_repeated_play_prisoners_dilemma(self):
        self.data_for_csv = []
        # Have every strategy play every other strategy with 6 game types
        for player_1_type in range(0, 9):
            for player_2_type in range(0, 9):
                self._play_6_game_types(player_1_type, player_2_type)
        labels = ["Player 1", "Player 2", "Number of Rounds",
                  "Game Type", "Player 1 Score", "Player 2 Score"]
        data = pandas.DataFrame.from_records(self.data_for_csv, columns=labels)
        data.to_csv("PrisonersDilemmaMatchData.csv",  sep=",")

    def _play_6_game_types(self, player_1_type, player_2_type):
        players = [Player(player_1_type, player_number=0),
                   Player(player_2_type, player_number=1)]
        game = Game(players)

        game_results = []
        game_results.append(game.playGame(game_type=0))
        game_results.append(game.playGame(game_type=1))
        game_results.append(game.playGame(game_type=2))
        # Repeat the beta game multiple times for better statistical accuracy
        # since beta games are non-deterministic
        for _ in range(0, 30):
            game_results.append(game.playGame(game_type=3))
            game_results.append(game.playGame(game_type=4))
            game_results.append(game.playGame(game_type=5))
        self._add_data_to_csv(game_results, game)

    def _add_data_to_csv(self, game_results, game):
        for game_result in game_results:
            csv_row = self._create_csv_row(game_result, game)
            self.data_for_csv.append(csv_row)

    def _create_csv_row(self, game_result, game):
        data_to_add = []
        player_1_strategy = self.names_of_strategies.get(
            game.players[0].player_type)
        player_2_strategy = self.names_of_strategies.get(
            game.players[1].player_type)
        data_to_add.append(player_1_strategy)
        data_to_add.append(player_2_strategy)
        results, rounds, game_type = game_result
        data_to_add.append(rounds)
        data_to_add.append(self.game_type.get(game_type))
        data_to_add.extend(AnalysisHelper.total_score(results))
        return data_to_add
