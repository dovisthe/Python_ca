import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# GridWorld klasė: sukuria aplinką, kurioje agentas mokysis
class GridWorld:
    def __init__(self, size=5, obstacles=[(1, 1), (2, 2), (3, 3)], start=(0, 0), goal=(4, 4)):
        self.size = size
        self.obstacles = obstacles
        self.start = start
        self.goal = goal
        self.reset()

    # reset metodas: grąžina agentą į pradinę padėtį
    def reset(self):
        self.position = self.start
        return self.position

    # step metodas: atlieka vieną agento žingsnį pagal veiksmą ir grąžina naują būseną, atlygį ir informaciją, ar tikslas pasiektas
    def step(self, action):
        if action == 0:  # Į viršų
            next_position = (self.position[0] - 1, self.position[1])
        elif action == 1:  # Į dešinę
            next_position = (self.position[0], self.position[1] + 1)
        elif action == 2:  # Žemyn
            next_position = (self.position[0] + 1, self.position[1])
        elif action == 3:  # Į kairę
            next_position = (self.position[0], self.position[1] - 1)

        # Tikriname, ar nauja pozicija yra galiojanti (ne už ribų ir ne kliūtis)
        if (0 <= next_position[0] < self.size and
                0 <= next_position[1] < self.size and
                next_position not in self.obstacles):
            self.position = next_position

        reward = -1  # Standartinis atlygys už žingsnį
        if self.position == self.goal:
            reward = 10  # Atlygys už tikslo pasiekimą
        elif self.position in self.obstacles:
            reward = -10  # Bauda už atsitrenkimą į kliūtį

        return self.position, reward, self.position == self.goal

    # render metodas: vizualizuoja GridWorld aplinką
    def render(self, q_table=None, ax=None):
        grid = np.zeros((self.size, self.size))
        for obs in self.obstacles:
            grid[obs] = -1
        grid[self.start] = 0.5
        grid[self.goal] = 1
        grid[self.position] = 0.8

        ax.clear()
        ax.imshow(grid, cmap='cool')
        if q_table is not None:
            for i in range(self.size):
                for j in range(self.size):
                    if (i, j) not in self.obstacles and (i, j) != self.goal:
                        action = np.argmax(q_table[i, j])
                        if action == 0:
                            ax.arrow(j, i, 0, -0.3, head_width=0.2, head_length=0.2)
                        elif action == 1:
                            ax.arrow(j, i, 0.3, 0, head_width=0.2, head_length=0.2)
                        elif action == 2:
                            ax.arrow(j, i, 0, 0.3, head_width=0.2, head_length=0.2)
                        elif action == 3:
                            ax.arrow(j, i, -0.3, 0, head_width=0.2, head_length=0.2)

# q_learning funkcija: įgyvendina Q-learning algoritmą
def q_learning(env, episodes=500, alpha=0.1, gamma=0.99, epsilon=0.1):
    """
    env: Aplinka, kurioje mokosi agentas.
    episodes: Epizodų skaičius, per kuriuos mokysis agentas (numatyta reikšmė 500).
    alpha: Mokymosi greitis, nurodantis, kiek agentas atnaujina savo Q reikšmes (numatyta reikšmė 0.1).
    gamma: Diskonto koeficientas, nurodantis būsimos naudos svarbą (numatyta reikšmė 0.99).
    epsilon: Epsilon-greedy politikos parametras, nurodantis atsitiktinių veiksmų tikimybę (numatyta reikšmė 0.1).
    """
    q_table = np.zeros((env.size, env.size, 4))  # Inicializuojame Q-table
    steps = []

    for episode in range(episodes):
        state = env.reset()  # Pradžioje kiekvieno epizodo atstatome agentą į pradinę padėtį
        done = False
        while not done:
            # Pasirenkame veiksmą naudojant epsilon-greedy politiką
            if np.random.uniform(0, 1) < epsilon:
                action = np.random.choice(4)
            else:
                action = np.argmax(q_table[state[0], state[1]])

            # Atliekame veiksmą ir gauname naują būseną bei atlygį
            next_state, reward, done = env.step(action)
            old_value = q_table[state[0], state[1], action]
            next_max = np.max(q_table[next_state[0], next_state[1]])

            # Atnaujiname Q-table pagal Q-learning taisyklę
            q_table[state[0], state[1], action] = old_value + alpha * (reward + gamma * next_max - old_value)

            state = next_state
            steps.append((q_table.copy(), env.position))  # Įrašome dabartinę Q-table būseną ir agento padėtį

    return q_table, steps

# update funkcija: atnaujina vizualizaciją kiekviename žingsnyje
def update(frame, env, ax):
    q_table, position = frame
    env.position = position
    env.render(q_table, ax)

# Paleidimas
env = GridWorld()
q_table, steps = q_learning(env)

fig, ax = plt.subplots()
ani = animation.FuncAnimation(fig, update, frames=steps, fargs=(env, ax), interval=100)
plt.show()
