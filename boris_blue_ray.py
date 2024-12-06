import random

import gym
from gym.envs.registration import register

import matplotlib.pyplot as plt
import networkx as nx
import time
from stable_baselines3 import PPO

random_input = [0,0]
blue_ray_output = [0,0]
X,Y,x,y = random_input[0],random_input[1],blue_ray_output[0],blue_ray_output[1]

# Define a custom environment for the game
class NeuronGameEnv(gym.Env):
    def __init__(self,X,Y,x,y):
        print("Initializing Neuron Game Environment...")
        self.neuron = self.Neuron(X, Y)  # Initialize Neuron with default x and y
        self.player = self.Player(x, y)  # Initialize Player with default x and y
        self.game = self.Game()

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
            self.set_player = [random.randint(0, 100), random.randint(0, 100)]
            print("Game initialized.")

        def add_neuron(self, x, y):
            neuron = Neuron(x, y)
            self.neurons.append(neuron)
            print(f"Neuron added at ({x}, {y}). Total neurons: {len(self.neurons)}")
            return neuron

        def set_player(self, x, y):
            self.player = self.player(x, y)
            print(f"Player set at ({x}, {y}).")

        def activate_neuron(self):
            random_neuron = random.choice(self.neurons)
            random_neuron.activate()
            for neuron in random_neuron.connections:
                neuron.activate()

        def connect_neurons(self, neuron1, neuron2):
            neuron1.connect(neuron2)
            neuron2.connect(neuron1)

        def start_game_timer(self):
            global timer
            while timer > 0:
                timer -= 1
                print(f"Timer: {timer}")
                if timer == 0:
                    self.is_game_over = True
                    print("Game over! Timer reached zero.")
                    break

        def game_state(self):
            state =  {
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
                "timer": timer,
                "is_game_over": self.is_game_over,
            }
            print(f"Game State: {state}")
            return state


        def reset(self):
            self.is_game_over = False
            for neuron in self.neurons:
                neuron.activated = False
                neuron.time_to_die = 30
                neuron.connections = []
            self.player.activate()
            print("Game reset.")


env = NeuronGameEnv(X,Y,x,y)
print("Initializing PPO...")
# Register the environment
register(
    id="blueray-v0",  # Unique name for the environment
    entry_point="__main__:NeuronGameEnv",  # Path to the environment class
)
# env = gym.make("blueray-v0",max_episode_steps=1,disable_env_checker=False, X=X, x=x , Y=Y, y=y)
env = gym.make("CartPole-v1",max_episode_steps=1,disable_env_checker=False,X=X, x=x , Y=Y, y=y)
observation, info = env.reset(seed=42)

for _ in range(1000):
    X, Y, x, y = random_input[0], random_input[1], blue_ray_output[0], blue_ray_output[1]
    # this is where you would insert your policy
    action = env.action_space.sample(X, Y, x, y)

    # step (transition) through the environment with the action
    # receiving the next observation, reward and if the episode has terminated or truncated
    observation, reward, terminated, truncated, info = env.step(action)

    # If the episode has ended then we can reset to start a new episode
    if terminated or truncated:
        observation, info = env.reset()

env.close()
    # Implement game state representation, actions, and rewards
game = env.Game()
neuron = env.Neuron(X,Y)
player = env.Player(x,y)
model = PPO("MlpPolicy", env, verbose=1)
model.learn(total_timesteps=10000)


# Use the model to make decisions
observation = env.reset()
action, _ = model.predict(observation)




def plot_neuron_graph(game):
    # Create a graph
    G = nx.Graph()

    # Add neurons as nodes to the graph
    for neuron in game.neurons:
        G.add_node((neuron.x, neuron.y), activated=neuron.activated)

    # Add connections as edges
    for neuron in game.neurons:
        for connected_neuron in neuron.connections:
            G.add_edge((neuron.x, neuron.y), (connected_neuron.x, connected_neuron.y))

    # Set up the plot
    plt.figure(figsize=(8, 8))

    # Draw the graph with node positions
    pos = {(neuron.x, neuron.y): (neuron.x, neuron.y) for neuron in game.neurons}
    nx.draw(G, pos, with_labels=False, node_size=100, node_color='yellow' if neuron.activated else 'gray',
            edge_color='gray')

    # Plot the player
    if game.player:
        plt.scatter(game.player.x, game.player.y, color='purple', s=100, label='Player')

    # Show the plot
    plt.title('Neuron Network with Player')
    plt.xlabel('X Position')
    plt.ylabel('Y Position')
    plt.legend()
    plt.show()


# Initialize PPO
# print("Initializing PPO...")
# g = PPO("blueray", env, verbose=1)

game = env.Game()
neuron = env.Neuron(X, Y)
player = env.Player(x, y)
model = PPO("blueray", env, verbose=1)
model.learn(total_timesteps=10000)

# Use the model to make decisions
print("Starting model predictions...")
observation = env.game_state()
action, _ = model.predict(observation)
print(f"Action taken: {action}")

# Start the game
timer = 30
game.reset()

for _ in range(10):
    x, y = random.randint(0, 100), random.randint(0, 100)
    game.add_neuron(x, y)

while not game.is_game_over:
    # Example usage
    timer -= 10
    game.set_player(random.randint(0,100), random.randint(0,100))


    # Connect some neurons
    for i in range(5):
        neuron1 = game.neurons[i]
        neuron2 = game.neurons[(i + 1) % len(game.neurons)]  # Circular connection
        game.connect_neurons(neuron1, neuron2)

    # Plot the graphx
    game.activate_neuron()
    plot_neuron_graph(game)
    print(timer, "seconds!")

# Calculate the start time
start = time.time()

# Code here

# Calculate the end time and time taken
end = time.time()
length = end - start

# Show the results : this can be altered however you like
print("game over")
game.is_game_over = False

env.close()