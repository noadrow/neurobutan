import random
from blue_ray import NeuronGameEnv

timer = 60

def input_system(action,game):
    global timer
    # Player input and action logic
    if action == 0:
        game.player.connect_to_neuron(sorted_neurons[0])
    elif action == 1:
        game.player.connect_to_neuron(sorted_neurons[1])
    elif action == 2:
        game.player.connect_to_neuron(sorted_neurons[2])
    elif action == 3:
        game.player.connect_to_neuron(sorted_neurons[3])

    game.player.update(state_log["player"])
    game.render(neurons)

    if state_log['player']['activated']:
        timer += 0.1
    else:
        timer -= 0.1

    if timer <= 0:
        print("game over")
        game.set_game_state(True)
    elif timer >= 60:
        print("you won!")
        game.set_game_state(True)

def ai_agent(state):
    return env.action_space.sample()  # Random action for demonstration

env = [0, 0, 50, 50]
timer = 60
env = NeuronGameEnv()  # Initialize environment with default parameters
game = env.Game()
pos = {"x": 50, "y": 50}

neurons = [
    {
        "x": random.randint(0, 100),
        "y": random.randint(0, 100),
        "activated": random.choice([True, False]),  # 50% chance of being True
        "time_to_die": 30
    }
    for _ in range(100)
]

_neurons = env.add_neurons(neurons=neurons, game=game)  # Add neurons to the environment
print("Generated Neurons:", neurons)

game_running = True
while game_running:
    picture = env.reset(game)
    state_log = picture.get_state()
    game_running = not state_log['is_game_over']
    print("Game state after reset:", state_log)

    for neuron in neurons:
        random_neuron = random.choice([n for n in neurons if n != neuron])  # Choose a different random neuron
        if "connections" not in neuron:
            neuron["connections"] = []  # Initialize connections if not already present
        if random_neuron not in neuron["connections"]:  # Avoid duplicate connections
            neuron["connections"].append(random_neuron)

    env.update_neurons(neurons=neurons, game=game)  # Assuming a method `update_neurons` exists
    game.render(neurons)

    player_x = state_log["player"]["x"]
    player_y = state_log["player"]["y"]

    pos = [player_x,player_y]

    sorted_neurons = sorted(
        neurons,
        key=lambda neuron: ((neuron["x"] - player_x) ** 2 + (neuron["y"] - player_y) ** 2) ** 0.5
    )
    action = ai_agent(state_log)
    input_system(action,game)

    next_state, reward, done, info = env.game.set_action(action)

    print(f"Action Taken: {action}")
    print(f"New State: {next_state}, Reward: {reward}, Done: {done}")

