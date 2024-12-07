import random
from blue_ray import NeuronGameEnv, plot_neuron_graph
import time

env = [0, 0, 50, 50]
if __name__ == "__main__":
    try:
        timer = 60
        env = NeuronGameEnv()  # Initialize environment with default parameters
        game = env.Game()
        pos = {"x": 50, "y": 50}

        try:
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

            _neurons = env.add_neurons(neurons=neurons,game=game)  # Add neurons to the environment
            print("Generated Neurons:", neurons)

        except Exception as e:
            print("Error during reset:", e)


        game_running = True
        while game_running:
            picture = env.reset(game)
            state_log = picture.get_state()
            game_running = not state_log['is_game_over']
            print("Game state after reset:", state_log)

            # Random connection update for neurons
            for neuron in neurons:
                random_neuron = random.choice([n for n in neurons if n != neuron])  # Choose a different random neuron
                if "connections" not in neuron:
                    neuron["connections"] = []  # Initialize connections if not already present
                if random_neuron not in neuron["connections"]:  # Avoid duplicate connections
                    neuron["connections"].append(random_neuron)
                    print(f"Neuron {neuron} connected to {random_neuron}.")

            # Render the updated neurons and game state
            env.update_neurons(neurons=neurons,game=game)  # Assuming a method `update_neurons` exists
            game.render(neurons)

            if state_log['player']['activated']:
                timer += 0.1
            else:
                game.render(neurons)
                timer -= 0.1

            if timer <= 0:
                print("game over")
                game.set_game_state(True)

    finally:
        print("succsess!")
