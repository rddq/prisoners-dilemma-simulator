import random 

class Player:
    
    def __init__(self, player_type, player_number):
        self.player_type = player_type
        self.player_number = player_number
        # 1 is defect, 0 is cooperate
        # Please make player number 0 or 1
        self.type_map = {
            0 : self.__our_strategy__,
            1 : self.__always_defect__,
            2 : self.__random__,
            3 : self.__always_cooperate__,
            4 : self.__tit_for_tat__,
            5 : self.__tit_for_two_tats__,
            6 : self.__pavlov_strategy__,
            7 : self.__win_stay_lose_shift__,
            8 : self.__never_forgive__
        }
        
    def play(self, results):
        # Below code works like a switch function
        func = self.type_map.get(self.player_type, lambda: "Invalid Player Type")
        return func(results)

    def __our_strategy__(self,results):
        pass

    def __always_defect__(self, results):
        return 1

    def __random__(self, results):
        return random.choice([0,1]) 

    def __always_cooperate__(self, results):
        return 0

    def __tit_for_tat__(self, results):
        if len(results) == 0:
            return 0

        return results[-1][not self.player_number]

    def __tit_for_two_tats__(self, results):
        if len(results) == 0 or len(results) == 1:
            return 0

        other_player = not self.player_number
        if results[-1][other_player] == 1 & results[-2][other_player] == 1:
            return 1
        else:
            return 0

    def __pavlov_strategy__(self, results):       
        if len(results) == 0:
            return 0
        
        other_player = not self.player_number
        if results[-1][other_player] != results[-1][self.player_number]:
            return 1
        else:
            return 0

    def __win_stay_lose_shift__(self, results):
        if len(results) == 0:
            self.choice = 0
            return self.choice

        other_player = not self.player_number
        if results[-1][other_player] != 0:
            self.choice = int(not self.choice)
        return self.choice
        
    def __never_forgive__(self, results):
        if len(results) == 0:
            self.triggered = 0
            return 0
        
        other_player = not self.player_number
        if results[-1][other_player] == 1:
            self.triggered = 1
        
        return self.triggered
