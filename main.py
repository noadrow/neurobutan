import blue_ray
import random
import random
import matplotlib.pyplot as plt
import networkx as nx

is_game_over = True

time = 60


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

    def move_right(self):
        self.x += 1

    def move_left(self):
        self.x -= 1

    def move_up(self):
        self.y += 1

    def move_down(self):
        self.y -= 1

    def action(self):
        options = [1,2,3,4]
        action = random.choice(throws)
        if action==1:
            self.move_up()
        if action==2:
            self.move_down()
        if action==3:
            self.move_right()
        if action==4:
            self.move_left()

#start game
game = blue_ray
action = 1
observation, info = game.br.reset(game,action)

for _ in range(1000):
    x, y = random.randint(0, 100), random.randint(0, 100)
    game.add_neuron(x, y)

    observation, reward, terminated, truncated, info = game.step(action)

    if terminated or truncated:
        observation, info = game.reset()
    #game.br.find_closest_neuron(game.br.)

game.close()