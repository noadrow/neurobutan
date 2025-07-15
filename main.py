import blue_ray
import random
import random
import matplotlib.pyplot as plt
import networkx as nx
from gemini_API import send_content

is_game_over = True

time = 60


class Player:
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
        if action==1:
            self.move_up()
        if action==2:
            self.move_down()
        if action==3:
            self.move_right()
        if action==4:
            self.move_left()
        if action==5:
            self.connect(env.find_closest_neuron(neurons))

#start game
env = blue_ray
game = blue_ray.Game()
action = 1
neurons = []

state = game.reset(action,neurons)
obs,neurons, is_game_over = state["player"],state["neurons"],state["is_game_over"]

for _ in range(1000):
    x, y = random.randint(0, 100), random.randint(0, 100)
    neurons.append(game.add_neuron(x, y))

i = 0
res = (f"sending you game state, your goal is to connect as much neurons to be activated. this is your current stat for round number {i} your action spcae is 1-5 answer only by one of those numbers:"
       f"1=up,2=down,3=right,4=left,5=connect to closest neuron")
while not is_game_over:
    i += 1

    obs = game.step(str(action))
    obs = game.reset(str(action),neurons)
    game.render(obs["neurons"])
    neurons_state = ""
    for neuron in obs["neurons"]:
        neurons_state += f"{neuron.x}, {neuron.y} , {neuron.activated}"
    player_state = obs["player"]
    action = send_content(res,f"round number {i}: your status:{player_state} neurons state: {neurons_state}")




game.close()