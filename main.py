import random
import matplotlib.pyplot as plt
import networkx as nx

time = 30

class Neuron:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.connections = []
        self.activated = False
        self.time_to_die = 30

    def activate(self):
        self.activated = True
        self.time_to_die += 10

    def connect(self, neuron):
        self.connections.append(neuron)

    def is_alive(self):
        return self.time_to_die > 0


class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.connections = []
        self.activated = False

    def activate(self):
        for neuron in self.connections:
            if neuron.activated:
                self.activated = True

    def connect_to_neuron(self, neuron):
        self.connections.append(neuron)
        if neuron.activated:
            self.activated = True

class Game:
    def __init__(self):
        self.neurons = []
        self.player = None
        self.is_game_over = False
        self.set_player(random.randint(0, 100), random.randint(0, 100))

    def add_neuron(self, x, y):
        neuron = Neuron(x, y)
        self.neurons.append(neuron)
        return neuron

    def set_player(self, x, y):
        self.player = Player(x, y)

    def activate_neuron(self):
        random_neuron = random.choice(self.neurons)
        random_neuron.activate()
        for neuron in random_neuron.connections:
            neuron.activate()

    def connect_neurons(self, neuron1, neuron2):
        neuron1.connect(neuron2)
        neuron2.connect(neuron1)

    def start_game_timer(self):
        global time
        while time > 0:
            time -= 1
            if time == 0:
                self.is_game_over = True
                break

    def game_state(self):
        return {
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
            "timer": time,
            "is_game_over": self.is_game_over,
        }

    def reset(self):
        self.is_game_over = False
        for neuron in self.neurons:
            neuron.activated = False
            neuron.time_to_die = 30
            neuron.connections = []
        self.player.activate()


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


#start game
game = Game()
game.reset()

for _ in range(10):
    x, y = random.randint(0, 100), random.randint(0, 100)
    game.add_neuron(x, y)

while not game.is_game_over:
    # Example usage
    time = time - 10
    game.set_player(random.randint(0,100), random.randint(0,100))



    # Connect some neurons
    for i in range(5):
        neuron1 = game.neurons[i]
        neuron2 = game.neurons[(i + 1) % len(game.neurons)]  # Circular connection
        game.connect_neurons(neuron1, neuron2)

    # Plot the graphx
    game.activate_neuron()
    plot_neuron_graph(game)

