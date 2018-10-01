import matplotlib.pyplot as plt
import numpy as np

class PlotHelper:
    def __init__(self):
        pass
    
    @staticmethod
    def __results_over_time__(player_results):
        #results_over_time = [sum(results[0:i]) for i in range(0,len(results))] 
        results_over_time = []
        for x in range(0,len(player_results)):
            sum1 = sum(player_results[0:x])
            results_over_time.append(sum1)
        return results_over_time

    @staticmethod
    def plot_player_rewards_over_time(results):
        results = np.array(results)
        p1_results = results[:,-2]
        p1_summation = PlotHelper.__results_over_time__(p1_results)
        p2_results = results[:,-1]
        p2_summation = PlotHelper.__results_over_time__(p2_results)
        
        fig, ax1 = plt.subplots()
        
        x = range(0,len(results))
        ax1.plot(x,p1_summation, label="Player 1 Reward", color='g')
        ax1.plot(x,p2_summation, label="Player 2 Reward", color='r')
        
        ax1.set_xlim(0,len(results)) 
        ax1.set_title('Cumulative Reward vs Round Number')

        ax1.set_xlabel('Round Number')
        ax1.set_ylabel('Reward')

        ax1.grid()
        ax1.legend()

        plt.show()
        # If it looks like there is only one line showing up, 
        # they are on top of each other