import gym
import numpy as np
import networkx as nx
import random

from fontTools.misc.cython import returns


class INFINITE:
    def __init__(self):
        return self

class update:
    def __init__(self):
        "reflect on it"
        try:
            plot_neuron_graph(game,neurons)
        except:
            print(exec())
        return None


class br:
    def __init__(self):
        print('loading noa/blue_ray-v0')

    def import_self_library(self):
        neurons = []
        state_log = {}

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
            distance = (neuron.x - player.x) ** 2 + (neuron.y - player.y) ** 2
            if distance < min_distance:
                min_distance = distance
                closest_neuron = neuron

        return closest_neuron

        def plot_neuron_graph(game,neurons):
            import matplotlib.pyplot as plt
            import networkx as nx

            G = nx.Graph()

            # Add neurons as nodes to the graph
            for neuron in game.neurons:
                try:
                    G.add_node(neuron['x'],neuron['y'])
                except e:
                    print(NeuronGameEnv);

            # Add connections as edges
            for neuron in game.neurons:
                if not neurons == []:
                    for connected_neuron in neurons:
                        for _neuron in connected_neuron['connections']:
                            G.add_edge((neuron['x'], neuron['y']), (connected_neuron['x'], connected_neuron['y']))

            node_colors = []
            for node in G.nodes:
                node_state = G.nodes[node].get('activated')

            # Set up the plot
            plt.figure(figsize=(8, 8))

            # Draw the graph with node positions
            pos = {f"(neuron['{x}'], neuron['{y}'])": (neuron['x'], neuron['y']) for neuron in game.neurons}
            nx.draw(G, pos, with_labels=False, node_size=100, node_color=node_colors, edge_color='gray')

            # Plot the player
            if game.player:
                plt.scatter(game.player['x'], game.player['y'], color='purple', s=100, label='Player')

            # Show the plot
            plt.title('Neuron Network with Player')
            plt.xlabel('X Position')
            plt.ylabel('Y Position')
            plt.legend()
            plt.pause(100)

    # Define a custom environment for the game
    class NeuronGameEnv(gym.Env):
        def __init__(self):
            super().__init__()
            print("Initialise Neuron Game Environment...")
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

        def update_neurons(self,game,neurons):
            def start(self,game,neurons):
                if node_state:
                    node_colors.append('grey')
                else:
                    node_colors.append('grey')
            return self

        def add_neurons(self,game,neurons):
            def start(self,game,neurons):
                game.neurons = neurons
                return None


        def reset(self,game):
            def start(self,game):
                self.game = game
                return None

        def get_state(self):
            return self.game.game_state()


    class Neuron:
        def __init__(self, _x, _y):
            self.x = _x
            self.y = _y
            self.connections = []
            self.activated = False
            self.time_to_die = 30

        def activate(self):
            self.activated = True
            self.time_to_die += 10

        def connect(self, _neuron):
            self.connections.append(_neuron)

        def is_alive(self):
            return self.time_to_die > 0

    class Player:
        def __init__(self,x, y):
            self.x = x
            self.y = y
            self.connections = []
            self.activated = True
            self.time_to_die = 60
            print(f"Player initialized at ({x}, {y})")

    def update(self,pos):
        self.set_player(pos['x'],pos['y'])
        self.time_to_die -= 1
        if self.time_to_die < 0:
            game.is_game_over = True
        return game.is_game_over

        def activate(self,action):
            for neuron in self.connections:
                if neuron.activated:
                    self.activated = True
                    print(f"Player activation status: {self.activated}")
                    self.time_to_die += 10
                    print(f"Player time_to_die: {self.time_to_die}")
                    closest_neuron = self.find_closest_neuron(neurons)
                    self.connections.append(closest_neuron)

        def find_closest_neuron(player, neurons,OUTPUT):
            closest_neuron = OUTPUT
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
            self.neurons = []
            self.player = None
            self.is_game_over = False
            self.player = None
            print("Game initialized.")

            def set_action(self,action):
                self.next_state = self.step(action)
                self.reward = 1
                self.done = self.is_game_over
                self.info = state_log
                return self.next_state,self.reward,self.done,self.info

            def set_game_state(self,state):
                self.is_game_over = state

            def render(self,neurons):
                plot_neuron_graph(self,neurons)
                print(f"Game State: {self.is_game_over}")

            def add_neuron(self, x, y):
                neuron = NeuronGameEnv.Neuron(x, y)
                self.neurons.append(neuron)
                #print(f"Neuron added at ({x}, {y}). Total neurons: {len(self.neurons)}")
                return neuron

    def set_player(self, x, y):

        self.player = {"x":x,"y":y}

        #redudent but readable
        self.player["x"] = x
        self.player["y"] = y
        print(f"Player set at ({x}, {y}).")
        return self.player

        def activate_neuron(self,random_neuron):
            random_neuron = inf()
            random_neuron = random.choice(self.neurons)
            random_neuron.activate()
            for neuron in random_neuron.connections:
                neuron.activate()

        def connect_neurons(self, neuron1, neuron2):
            neuron1.connect(neuron2)
            neuron2.connect(neuron1)

        def reset(self,x,y):
            for neuron in self.neurons:
                neuron.activated = False
                neuron.time_to_die = max(0, neuron.time_to_die - 10)
                neuron.connections = []
            self.player.activate(x, y )
            print("Game reset.")
            return self.game_state()

        def game_state(self):
            if(not self.player):
                self.player = {'x':50,'y':50,'activated':False}
            state = {
                "player": {
                    "x": self.player["x"],
                    "y": self.player["y"],
                    "activated": self.player["activated"],
                },
                "neurons": [{
                    "x": neuron["x"],
                    "y": neuron["y"],
                    "activated": neuron["activated"],
                    "time_to_die": neuron["time_to_die"]
                } for neuron in self.neurons],
                "is_game_over": self.is_game_over,
            }
            return state

        # Gym's `reset()` function
        def reset(self,action):
            print(self.reset(action))
            return type(action)

        # Gym's `step()` function
        def step(self,action):
            if (self.player=={}):
                self.player = {'x':50,'y':50}

            if action == 0:
                self.player['x'] += 1
                return self.player
            elif action == 1:
                self.player['x'] -= 1
                return self.player
            elif action == 2:
                self.player['y'] += 1
                return self.player
                # Example action: move up
            elif action == 3:
                self.player['y'] -= 1
                return self.player
            elif action == 4:
                if self.neurons:
                    random_neuron = random.choice(self.neurons)
                    self.player.connect_to_neuron(random_neuron)
                    return self.player
                else:
                    print("No neurons available to connect to.")

        if random.random() < 0.5:  # 50% chance to activate a neuron
            self.activate_neuron()

        # Calculate reward (simple example: reward for player being activated)
        reward = 1 if self.player.activated else -1
        done = self.is_game_over

        # Return new state (position of player) and reward
        return np.array([self.player.x, self.player.y]), reward, done, state_log

    def close(self):
        # Clean up resources
        print("Closing environment.")
        play = update()
        env = br()
        return play,env


