import random
from blue_ray import NeuronGameEnv, plot_neuron_graph
import time

env = [0, 0, 50, 50]
if __name__ == "__main__":
    try:
        timer = 60
        env = NeuronGameEnv()  # Initialize environment with default parameters
        game = env.Game()
        pos = {"x": 50, "y": 50}

        try:
            state = env.reset(game)
            print("Game state after reset:", state)
        except Exception as e:
            print("Error during reset:", e)
    finally:
        print("succsess!")
