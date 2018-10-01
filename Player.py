import random 

class Player:
    
    def __init__(self, player_type, player_number):
        self.player_type = player_type
        self.player_number = player_number
        # 1 is defect, 0 is cooperate
        # Please make player number 0 or 1
        self.type_map = {
            1 : self.always_defect,
            2 : self.random,
            3 : self.always_cooperate,
            4 : self.tit_for_tat,
            5 : self.tit_for_two_tats,
            6 : self.pavlov_strategy,
            7 : self.win_stay_lose_shift,
            8 : self.never_forgive
        }
        
    def play(self, results):
        # Below code works like a switch function
        func = self.type_map.get(self.player_type, lambda: "Invalid Player Type")
        return func(results)

    def always_defect(self, results):
        return 1

    def random(self, results):
        return random.uniform(0,1) 

    def always_cooperate(self, results):
        return 0

    def tit_for_tat(self, results):
        if len(results) == 0:
            return 1

        return results[-1][not self.player_number]

    def tit_for_two_tats(self, results):
        if len(results) == 0:
            return 1

        other_player = not self.player_number
        if results[-1][other_player] == 1 & results[-2][other_player] == 1:
            return 1
        else:
            return 0

    def pavlov_strategy(self, results):
        other_player = not self.player_number
        if len(results) == 0:
            return 1
        if results[-1][other_player] != results[-1][self.player_number]:
            return 1
        else:
            return 0

    def win_stay_lose_shift(self, results):
        pass

    def never_forgive(self, results):
        if len(results) == 0:
            self.triggered = 0
            return 1
        
        other_player = not self.player_number
        if results[-1][other_player] == 1:
            self.triggered = 1
        
        return self.triggered
