import random
from blue_ray import NeuronGameEnv, plot_neuron_graph
import time

env = [0, 0, 50, 50]
if __name__ == "__main__":
    try:
        timer = 60
        env = NeuronGameEnv()  # Initialize environment with default parameters
        game = env.Game()

        # Set up the player
        player = game.set_player(x=50,y=50)

        # Add neurons to the game
        for _ in range(5):
            _x, _y = random.randint(0, 100), random.randint(0, 100)  # Generate random positions
            game.add_neuron(_x, _y)

        # Visualize the game
        action = {'x': 50, 'y': 50}
        state = False
        while not state:
            neurons = game.neurons
            state = game.player.update(action)

            game.reset(action)
            game.render()
            timer -= 10

            if(timer > 0):
                action = game.step(action={50,50})
            else:
                game.close()



    except NameError as e:

        print(f"Error: {e}")
    except Exception as ex:
        print(f"An error occurred: {ex}")

    finally:
        print("system failed succsessfully!")

