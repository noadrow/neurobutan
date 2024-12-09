import random
import blue_ray  # יש לוודא שמודול זה קיים
import blue_ray as br
from networkx.generators.random_graphs import dual_barabasi_albert_graph


# פונקציה שמבצעת את אתחול המשחק
def main():
    try:
        # אתחול של השחקן והמפה
        blue_ray.set_player(br, x=50, y=50)
        blue_ray.plot_neuron_graph()  # הצגת גרף של נוירונים
        game = blue_ray.br.NeuronGameEnv

        # יצירת 100 נוירונים רנדומליים והכנסתם למשחק
        for i in range(100):
            _x, _y = random.random() * 100, random.random() * 100
            blue_ray.br.Neuron(_x, _y)
        print("100 neuron enter the game")

    except Exception as e:
        print(f"Error: {e}")

    timer = 60
    game_running = True

    # יצירת מצב התחלתי של נוירונים
    neurons = [
        {
            "x": random.randint(0, 100),
            "y": random.randint(0, 100),
            "activated": random.choice([True, False]),  # 50% סיכוי להיות מופעל
            "time_to_die": 30
        }
        for _ in range(6)
    ]

    _neurons = blue_ray.add_neurons(neurons=neurons, game=game)  # הוספת נוירונים למשחק
    print("Generated Neurons:", neurons)

    while game_running:
        picture = blue_ray.reset(game)
        state_log = picture.get_state()
        game_running = not state_log['is_game_over']
        print("Game state after reset:", state_log)

        # עדכון קשרים רנדומליים בין נוירונים
        for neuron in neurons:
            random_neuron = random.choice([n for n in neurons if n != neuron])
            if "connections" not in neuron:
                neuron["connections"] = []  # אם לא הוגדר קשר, אתחל את הרשימה
            if random_neuron not in neuron["connections"]:
                neuron["connections"].append(random_neuron)

        # עדכון הנוירונים וציור המצב החדש
        env.update_neurons(neurons=neurons, game=game)  # עדכון מצב הנוירונים
        game.render(neurons)

        # פעולת השחקן
        action = ai_agent(state_log)  # בחירת פעולה אוטומטית
        input_system(action, game)  # עדכון פעולה למשחק

        # פעולה שבוצעה במשחק
        next_state, reward, done, info = env.game.set_action(action)
        print(f"Action Taken: {action}")
        print(f"New State: {next_state}, Reward: {reward}, Done: {done}")


# הרצת הקוד בתנאים הנכונים
if __name__ == "__main__":
    main()
