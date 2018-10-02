from numpy.random import choice
class Game:
    
    def __init__(self, players, bias=None):     
        self._results = []
        self._players = players
        self._bias = bias
        self._reward = {
            # Both Cooperate
            (0,0):[3,3],
            # P1 Cooperate, P2 Defect
            (0,1):[1,5],
            # P1 Defect, P2 Cooperate
            (1,0):[5,1],
            # Both Defect
            (1,1):[2,2]
        }
    
    def playGame(self, iterations):
        results = self._results       
        count = 0
        while count < iterations:
            curr_round = []           
            for player in self._players:
                action = player.play(results)
                curr_round.append(action)
            self.__add_scores(curr_round) 
            results.append(curr_round)
            count += 1           
            if self._bias is not None:
                end_game = self.__flip_biased_coin(self._bias)
                if end_game:
                    break
        return results                    

    def __add_scores(self, curr_round):
        p1_played = curr_round[0]
        p2_played = curr_round[1]
        played = (p1_played, p2_played)
        rewards = self._reward.get(played)
        curr_round.extend(rewards)

    def __flip_biased_coin(self, bias):
        return choice([0,1],p=[self._bias,1-self._bias])

         





