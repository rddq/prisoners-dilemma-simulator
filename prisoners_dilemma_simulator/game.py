from numpy.random import choice


class Game:
    def __init__(self, players):
        self.players = players
        self._reward = {
            # Both Cooperate
            (0, 0): [3, 3],
            # P1 Cooperate, P2 Defect
            (0, 1): [1, 5],
            # P1 Defect, P2 Cooperate
            (1, 0): [5, 1],
            # Both Defect
            (1, 1): [2, 2]
        }
        self._game_set_up_methods = {
            0: self.set_up_type_0,
            1: self.set_up_type_1,
            2: self.set_up_type_2,
            3: self.set_up_type_3,
            4: self.set_up_type_4,
            5: self.set_up_type_5
        }

    def playGame(self, game_type):
        func = self._game_set_up_methods.get(
            game_type, lambda: "Invalid Game Type")
        iterations, beta = func()
        rounds = 0
        results = []
        count = 0
        while count < iterations:
            curr_round = []
            for player in self.players:
                action = player.play(results)
                curr_round.append(action)
            self._add_scores(curr_round)
            results.append(curr_round)
            count += 1
            rounds += 1
            if beta is not None:
                end_game = self._flip_biased_coin(beta)
                if end_game:
                    break
        return results, rounds, game_type

    def set_up_type_0(self):
        iterations = 5
        beta = None
        return [iterations, beta]

    def set_up_type_1(self):
        iterations = 100
        beta = None
        return [iterations, beta]

    def set_up_type_2(self):
        iterations = 200
        beta = None
        return [iterations, beta]

    def set_up_type_3(self):
        beta = 0.75
        iterations = 10000
        return [iterations, beta]

    def set_up_type_4(self):
        beta = 0.95
        iterations = 10000
        return [iterations, beta]

    def set_up_type_5(self):
        iterations = 10000
        beta = 0.99
        return [iterations, beta]

    def _add_scores(self, curr_round):
        p1_played = curr_round[0]
        p2_played = curr_round[1]
        played = (p1_played, p2_played)
        rewards = self._reward.get(played)
        curr_round.extend(rewards)

    def _flip_biased_coin(self, bias):
        return choice([0, 1], p=[bias, 1-bias])
