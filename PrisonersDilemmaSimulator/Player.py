import random 

class Player:
    
    def __init__(self, player_type, player_number):
        self._player_type = player_type
        self._player_number = player_number
        # 1 is defect, 0 is cooperate
        # Please make player number 0 or 1
        self._type_map = {
            0 : self.__our_strategy,
            1 : self.__always_defect,
            2 : self.__random,
            3 : self.__always_cooperate,
            4 : self.__tit_for_tat,
            5 : self.__tit_for_two_tats,
            6 : self.__pavlov_strategy,
            7 : self.__win_stay_lose_shift,
            8 : self.__never_forgive
        }
        
    def play(self, results):
        # Below code works like a switch function
        func = self._type_map.get(self._player_type, lambda: "Invalid Player Type")
        return func(results)

    def __our_strategy(self,results):
        return 1

    def __always_defect(self, results):
        return 1

    def __random(self, results):
        return random.choice([0,1]) 

    def __always_cooperate(self, results):
        return 0

    def __tit_for_tat(self, results):
        if len(results) == 0:
            return 0
        return results[-1][not self._player_number]

    def __tit_for_two_tats(self, results):
        if len(results) == 0 or len(results) == 1:
            return 0
        other_player = not self._player_number
        if results[-1][other_player] == 1 & results[-2][other_player] == 1:
            return 1
        else:
            return 0

    def __pavlov_strategy(self, results):       
        if len(results) == 0:
            return 0        
        other_player = not self._player_number
        if results[-1][other_player] != results[-1][self._player_number]:
            return 1
        else:
            return 0

    def __win_stay_lose_shift(self, results):
        if len(results) == 0:
            self.choice = 0
            return self.choice
        other_player = not self._player_number
        if results[-1][other_player] != 0:
            self.choice = int(not self.choice)
        return self.choice
        
    def __never_forgive(self, results):
        if len(results) == 0:
            self.triggered = 0
            return 0       
        other_player = not self._player_number
        if results[-1][other_player] == 1:
            self.triggered = 1        
        return self.triggered
