import random
from blue_ray import NeuronGameEnv

timer = 60

def input_system(action):
    global timer
    # Player input and action logic
    if action == 0:
        state_log["player"]["x"] = sorted_neurons[0]['x']
        state_log["player"]["y"] = sorted_neurons[0]['y']
    elif action == 1:
        state_log["player"]["x"] = sorted_neurons[1]['x']
        state_log["player"]["y"] = sorted_neurons[1]['y']
    elif action == 2:
        state_log["player"]["x"] = sorted_neurons[2]['x']
        state_log["player"]["y"] = sorted_neurons[2]['y']
    elif action == 3:
        state_log["player"]["x"] = sorted_neurons[3]['x']
        state_log["player"]["y"] = sorted_neurons[3]['y']

    game.player.update(state_log["player"])
    #game.render(neurons)

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
    # Logic for selecting an action; replace with a model if needed
    # For example, if actions are discrete integers:
    return env.action_space.sample()  # Random action for demonstration

env = [0, 0, 50, 50]
timer = 60
env = NeuronGameEnv()  # Initialize environment with default parameters
game = env.Game()
pos = {"x": 50, "y": 50}

# Generate 6 neurons with the specified properties
neurons = [
    {
        "x": random.randint(0, 100),
        "y": random.randint(0, 100),
        "activated": random.choice([True, False]),  # 50% chance of being True
        "time_to_die": 30
    }
    for _ in range(6)
]

_neurons = env.add_neurons(neurons=neurons, game=game)  # Add neurons to the environment
print("Generated Neurons:", neurons)

game_running = True
while game_running:
    picture = env.reset(game)
    state_log = picture.get_state()
    game_running = state_log['is_game_over']
    print("Game state after reset:", state_log)

    # Random connection update for neurons
    for neuron in neurons:
        random_neuron = random.choice([n for n in neurons if n != neuron])  # Choose a different random neuron
        if "connections" not in neuron:
            neuron["connections"] = []  # Initialize connections if not already present
        if random_neuron not in neuron["connections"]:  # Avoid duplicate connections
            neuron["connections"].append(random_neuron)

    # Render the updated neurons and game state
    env.update_neurons(neurons=neurons, game=game)  # Assuming a method `update_neurons` exists
    game.render(neurons)

    # Assume the player's current position is given by state_log["player"]["x"] and state_log["player"]["y"]
    player_x = state_log["player"]["x"]
    player_y = state_log["player"]["y"]

    pos = [player_x,player_y]

    # Calculate distance and sort neurons
    sorted_neurons = sorted(
        neurons,
        key=lambda neuron: ((neuron["x"] - player_x) ** 2 + (neuron["y"] - player_y) ** 2) ** 0.5
    )
    action = ai_agent(state_log)
    input_system(action)

    if __name__ == "__main__":
        try:
            print("ok")

            # Perform the action
            next_state, reward, done, info = env.step(action)

            # Print details
            print(f"Action Taken: {action}")
            print(f"New State: {next_state}, Reward: {reward}, Done: {done}")

            # Update state
            state = next_state

        except:


            print("succsess!")


