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
        for _ in range(100):
            _x, _y = random.randint(0, 100), random.randint(0, 100)  # Generate random positions
            game.add_neuron(_x, _y)

        # Visualize the game
        while True:
            plot_neuron_graph(game)
            game.reset()

        print("NeuronGameEnv initialized successfully!")
    except NameError as e:
        print(f"Error: {e}")
    except Exception as ex:
        print(f"An error occurred: {ex}")

