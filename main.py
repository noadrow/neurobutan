import random
from blue_ray import NeuronGameEnv, plot_neuron_graph

env = [0, 0, 0, 0]
if __name__ == "__main__":
    try:
        env = NeuronGameEnv()  # Initialize environment with default parameters
        game = env.Game()

        # Set up the player
        player = game.set_player(x=50,y=50)

        # Add neurons to the game
        for _ in range(5):
            _x, _y = random.randint(0, 100), random.randint(0, 100)  # Generate random positions
            game.add_neuron(_x, _y)

        # Visualize the game
        action = [50, 50]
        state = False
        while not state:
            print(action)
            neurons = game.neurons
            state = game.player.update(game)
            game.step(action)
            game.render(action,neurons)
            game.reset(action)

        print("well done!")
        game.close()

    except NameError as e:

        print(f"Error: {e}")
    except Exception as ex:
        print(f"An error occurred: {ex}")

