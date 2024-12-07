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
            game_running = True
            while game_running:
                picture = env.reset(game)
                state_log = picture.get_state()
                game_running = not state_log['is_game_over']
                print("Game state after reset:", state_log)
                if state_log['player']['activated']:
                    timer += 1
                else:
                    timer -= 1

                if timer <= 0:
                    print("game over")
                    game.set_game_state(True)

        except Exception as e:
            print("Error during reset:", e)
    finally:
        print("succsess!")
