from prisoners_dilemma_simulator.simulator import Simulator
from prisoners_dilemma_simulator.analysis_helper import PlotHelper

def main():
    sim = Simulator()
    sim.simulate_repeated_play_prisoners_dilemma()

if __name__ == '__main__':
    main()