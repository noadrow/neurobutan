import gym
import random
import numpy as np


# Define a custom environment for the game
class NeuronGameEnv(gym.Env):
    def __init__(self, X, Y, x, y):
        super().__init__()
        print("Initializing Neuron Game Environment...")
        self.neuron = self.Neuron(X, Y)  # Initialize Neuron with default x and y
        self.player = self.Player(x, y)  # Initialize Player with default x and y
        self.game = self.Game()
        self.id = "noa/blueray-v0"
        self.reward_threshold = 200
        self.max_episode_steps = 100
        self.disable_env_checker = True

        # Define action and observation spaces
        self.action_space = gym.spaces.Discrete(4)  # Example: 4 possible actions (up, down, left, right)
        self.observation_space = gym.spaces.Box(low=0, high=100, shape=(2,),
                                                dtype=np.int32)  # Example: player x, y positions

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
            neuron = NeuronGameEnv.Neuron(x, y)
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

        def reset(self):
            self.is_game_over = False
            for neuron in self.neurons:
                neuron.activated = False
                neuron.time_to_die = 30
                neuron.connections = []
            self.player.activate()
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
    def reset(self):
        self.game.reset()
        return np.array([self.game.player.x, self.game.player.y])

    # Gym's `step()` function
    def step(self, action):
        if action == 0:
            self.game.player.x += 1  # Example action: move right
        elif action == 1:
            self.game.player.x -= 1  # Example action: move left
        elif action == 2:
            self.game.player.y += 1  # Example action: move up
        elif action == 3:
            self.game.player.y -= 1
        elif action == 4:
            if self.game.neurons:
                random_neuron = random.choice(self.game.neurons)
                self.game.player.connect_to_neuron(random_neuron)
            else:
                print("No neurons available to connect to.")

        self.game.activate_neuron()  # Example: activate a random neuron

        # Calculate reward (simple example: reward for player being activated)
        reward = 1 if self.game.player.activated else -1
        done = self.game.is_game_over

        # Return new state (position of player) and reward
        return np.array([self.game.player.x, self.game.player.y]), reward, done, {}

    def render(self):
        # Optional: render the game state visually
        print(f"Player is at ({self.game.player.x}, {self.game.player.y})")
        print(f"Game over: {self.game.is_game_over}")

    def close(self):
        # Clean up resources
        print("Closing environment.")



X,Y,x,y = 0,0,0,0
game = NeuronGameEnv(X,Y,x,y)

for _ in range(100):
    x, y = random.randint(0, 100), random.randint(0, 100)  # Generate random positions
    game.add_neuron(x, y)