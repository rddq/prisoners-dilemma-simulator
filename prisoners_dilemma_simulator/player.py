import random


class Player:

    def __init__(self, player_type, player_number):
        self.player_type = player_type
        self._player_number = player_number
        # 1 is defect, 0 is cooperate
        # Please make player number 0 or 1
        self._type_map = {
            0: self._our_strategy,
            1: self._always_defect,
            2: self._random,
            3: self._always_cooperate,
            4: self._tit_for_tat,
            5: self._tit_for_two_tats,
            6: self._pavlov_strategy,
            7: self._win_stay_lose_shift,
            8: self._never_forgive
        }

    def play(self, results):
        # Below code works like a switch function
        func = (
            self._type_map.get(self.player_type, lambda: "Invalid Player Type")
        )
        return func(results)

    def _our_strategy(self, results):
        # 2TfT--only forgives if the other player cooperates twice
        if len(results) == 0:
            return 0
        other_player = not self._player_number
        if len(results) == 1:
            return results[-1][other_player]
        if results[-1][other_player] == 0 and results[-2][other_player] == 0:
            return 0
        return 1
        # Other options:
        #  Introduce a probability of forgiveness

    def _always_defect(self, results):
        return 1

    def _random(self, results):
        return random.choice([0, 1])

    def _always_cooperate(self, results):
        return 0

    def _tit_for_tat(self, results):
        if len(results) == 0:
            return 0
        return results[-1][not self._player_number]

    def _tit_for_two_tats(self, results):
        if len(results) == 0 or len(results) == 1:
            return 0
        other_player = not self._player_number
        if results[-1][other_player] == 1 & results[-2][other_player] == 1:
            return 1
        else:
            return 0

    def _pavlov_strategy(self, results):
        if len(results) == 0:
            return 0
        other_player = not self._player_number
        if results[-1][other_player] != results[-1][self._player_number]:
            return 1
        else:
            return 0

    def _win_stay_lose_shift(self, results):
        if len(results) == 0:
            self.choice = 0
            return self.choice
        other_player = not self._player_number
        if results[-1][other_player] != 0:
            self.choice = int(not self.choice)
        return self.choice

    def _never_forgive(self, results):
        if len(results) == 0:
            self.triggered = 0
            return 0
        other_player = not self._player_number
        if results[-1][other_player] == 1:
            self.triggered = 1
        return self.triggered
