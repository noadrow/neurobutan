import gym
import random
import numpy as np
from networkx import interval_graph

print('loading blue_ray')
neurons = []

def find_closest_neuron(player, neurons):
    """
    Find the closest neuron to the player's position.

    Args:
        player (Player): The player object with x, y coordinates.
        neurons (list of Neuron): The list of all neuron objects in the game.

    Returns:
        Neuron: The neuron closest to the player's position.
    """
    closest_neuron = None
    min_distance = float('inf')  # Start with an infinitely large distance

    for neuron in neurons:
        # Calculate the squared Euclidean distance
        distance = (neuron.x - player.x) ** 2 + (neuron.y - player.y) ** 2
        if distance < min_distance:
            min_distance = distance
            closest_neuron = neuron

    return closest_neuron


def plot_neuron_graph(game):
    import matplotlib
    import matplotlib.pyplot as plt
    matplotlib.use('TkAgg')
    import networkx as nx
    # Create a graph
    G = nx.Graph()

    # Add neurons as nodes to the graph
    for neuron in game.neurons:
        G.add_node((neuron.x, neuron.y), activated=neuron.activated)

    # Add connections as edges
    for neuron in game.neurons:
        if (neuron.connections==[]):
            neuron.connections = game.neurons[0],game.neurons[1]
        for connected_neuron in neuron.connections:
            G.add_edge((neuron.x, neuron.y), (connected_neuron.x, connected_neuron.y))

    # Set up the plot
    plt.figure(figsize=(8, 8))

    # Draw the graph with node positions
    pos = {(neuron.x, neuron.y): (neuron.x, neuron.y) for neuron in game.neurons}

    data = {'activated':neuron.activated}
    node_colors = ['yellow' if data['activated'] else 'gray' for _, data in G.nodes(data=True)]
    nx.draw(G, pos, with_labels=False, node_size=100, node_color=node_colors, edge_color='gray')

    # Plot the player
    if game.player:
        plt.scatter(game.player.x, game.player.y, color='purple', s=100, label='Player')

    # Show the plot
    plt.title('Neuron Network with Player')
    plt.xlabel('X Position')
    plt.ylabel('Y Position')
    plt.legend('Player')
    plt.pause(100)

# Define a custom environment for the game
class NeuronGameEnv(gym.Env):
    def __init__(self):
        super().__init__()
        print("Initialiself.Neuron(X, Y)zing Neuron Game Environment...")
        self.neuron = None  # Initialize Neuron with default x and y
        self.player = None # Initialize Player with default x and y
        self.game = self.Game()
        self.id = "noa/blueray-v0"
        self.reward_threshold = 200
        self.max_episode_steps = 100
        self.disable_env_checker = True

        # Define action and observation spaces
        self.action_space = gym.spaces.Discrete(4)  # Example: 4 possible actions (up, down, left, right)
        self.observation_space = gym.spaces.Box(low=0, high=100, shape=(2,),
                                                dtype=np.int32)  # Example: player x, y positions
        return None

    class Neuron:
        def __init__(self, _x, _y):
            self.x = _x
            self.y = _y
            self.connections = []
            self.activated = False
            self.time_to_die = 30
            print(f"Created Neuron at ({_x}, {_y})")

        def activate(self):
            self.activated = True
            self.time_to_die += 10
            print(f"Neuron at ({self.x}, {self.y}) activated. Time to die increased to {self.time_to_die}.")

        def connect(self, _neuron):
            self.connections.append(_neuron)
            print(f"Neuron at ({self.x}, {self.y}) connected to Neuron at ({_neuron.x}, {_neuron.y}).")

        def is_alive(self):
            return self.time_to_die > 0

    class Player:
        def __init__(self, x, y):
            self.x = x
            self.y = y
            self.connections = []
            self.activated = False
            print(f"Player initialized at ({x}, {y})")

        def activate(self):
            for neuron in self.connections:
                if neuron.activated:
                    self.activated = True
            print(f"Player activation status: {self.activated}")
            closest_neuron = self.connect_to_nearest_neuron(neurons)
            self.connections.append(closest_neuron)

        def find_closest_neuron(player, neurons):
            """
            Find the closest neuron to the player's position.

            Args:
                player (Player): The player object with x, y coordinates.
                neurons (list of Neuron): The list of all neuron objects in the game.

            Returns:
                Neuron: The neuron closest to the player's position.
            """
            closest_neuron = None
            min_distance = float('inf')  # Start with an infinitely large distance

            for neuron in neurons:
                # Calculate the squared Euclidean distance
                distance = (neuron.x - player.x) ** 2 + (neuron.y - player.y) ** 2
                if distance < min_distance:
                    min_distance = distance
                    closest_neuron = neuron

            return closest_neuron

        def connect_to_neuron(self, neuron):
            self.connections.append(neuron)
            if neuron.activated:
                self.activated = True
            print(f"Player connected to Neuron at ({neuron.x}, {neuron.y}). Player activated: {self.activated}")

    class Game:
        def __init__(self):
            import random
            self.neurons = []
            self.player = None
            self.is_game_over = False
            self.player = self.set_player
            print("Game initialized.")

        def render(self):
            plot_neuron_graph(self)

        def add_neuron(self, x, y):
            neuron = NeuronGameEnv.Neuron(x, y)
            self.neurons.append(neuron)
            #print(f"Neuron added at ({x}, {y}). Total neurons: {len(self.neurons)}")
            return neuron

        def set_player(self, x, y):
            import random
            x = random.randint(0, 100)
            y = random.randint(0, 100)
            self.player = NeuronGameEnv.Player(x, y)
            print(f"Player set at ({x}, {y}).")
            return self.player

        def activate_neuron(self):
            random_neuron = random.choice(self.neurons)
            random_neuron.activate()
            for neuron in random_neuron.connections:
                neuron.activate()

        def connect_neurons(self, neuron1, neuron2):
            neuron1.connect(neuron2)
            neuron2.connect(neuron1)

        def reset(self,action,neurons):
            self.is_game_over = False
            for neuron in self.neurons:
                neuron.activated = False
                neuron.time_to_die = 30
                neuron.connections = []
            action1, action2 = action[0],action[1]
            self.player.activate(action1,action2)
            print("Game reset.")
            return self.game_state()

        def game_state(self):
            state = {
                "player": {
                    "x": self.player.x,
                    "y": self.player.y,
                    "activated": self.player.activated,
                },
                "neurons": [{
                    "x": neuron.x,
                    "y": neuron.y,
                    "activated": neuron.activated,
                    "time_to_die": neuron.time_to_die
                } for neuron in self.neurons],
                "is_game_over": self.is_game_over,
            }
            return state

    # Gym's `reset()` function
    def reset(self,action):
        print(self.game.reset(action))
        return np.array([self.game.player.x, self.game.player.y])

    # Gym's `step()` function
    def step(self, action):
        i = 0
        print(f"step {i}")
        if action == 0:
            self.game.player.x += 1
            self.game.activate_neuron()  # Example: activate a random neuron
            print(self.game.player.x)
        elif action == 1:
            self.game.player.x -= 1
            print(self.game.player.x)
            # Example action: move left
        elif action == 2:
            self.game.player.y += 1
            print(self.game.player.y)
            # Example action: move up
        elif action == 3:
            self.game.player.y -= 1
            print(self.game.player.y)
        elif action == 4:
            if self.game.neurons:
                random_neuron = random.choice(self.game.neurons)
                self.game.player.connect_to_neuron(random_neuron)
            else:
                print("No neurons available to connect to.")

        if random.random() < 0.5:  # 50% chance to activate a neuron
            self.game.activate_neuron()

        # Calculate reward (simple example: reward for player being activated)
        reward = 1 if self.game.player.activated else -1
        done = self.game.is_game_over

        # Return new state (position of player) and reward
        return np.array([self.game.player.x, self.game.player.y]), reward, done, {}

    def render(self):
        plot_neuron_graph(self.game)
        print(f"Player 'mouse' is at ({self.game.player.x}, {self.game.player.y})")
        print(f"Game over: {self.game.is_game_over}")

    def close(self):
        # Clean up resources
        print("Closing environment.")

