import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.animation as animation

# Game parameters
GRID_WIDTH = 10
GRID_HEIGHT = 10
ACTIONS = [-1, 0, 1]  # Left, Stay, Right

class FruitCatchGame:
    def __init__(self):
        self.reset()

    def reset(self):
        self.basket_position = GRID_WIDTH // 2
        self.fruit_position = np.random.randint(0, GRID_WIDTH)
        self.fruit_row = 0
        return self.get_state()

    def step(self, action):
        # Move basket
        self.basket_position = max(0, min(GRID_WIDTH - 1, self.basket_position + action))

        # Move fruit down
        self.fruit_row += 1

        # Check if fruit is caught or missed
        if self.fruit_row == GRID_HEIGHT - 1:
            if self.basket_position == self.fruit_position:
                reward = 1  # Fruit caught
            else:
                reward = -1  # Fruit missed
            done = True
        else:
            reward = 0
            done = False

        return self.get_state(), reward, done

    def get_state(self):
        return (self.basket_position, self.fruit_position, self.fruit_row)

class QLearningAgent:
    def __init__(self, state_space, action_space, learning_rate=0.1, discount_factor=0.95, epsilon=0.1):
        self.q_table = {}
        self.lr = learning_rate
        self.gamma = discount_factor
        self.epsilon = epsilon
        self.action_space = action_space

    def get_action(self, state):
        if np.random.random() < self.epsilon:
            return np.random.choice(self.action_space)
        return self.get_best_action(state)

    def get_best_action(self, state):
        if state not in self.q_table:
            self.q_table[state] = np.zeros(len(self.action_space))
        return np.argmax(self.q_table[state])

    def update(self, state, action, reward, next_state):
        if state not in self.q_table:
            self.q_table[state] = np.zeros(len(self.action_space))
        if next_state not in self.q_table:
            self.q_table[next_state] = np.zeros(len(self.action_space))

        best_next_action = self.get_best_action(next_state)
        td_target = reward + self.gamma * self.q_table[next_state][best_next_action]
        td_error = td_target - self.q_table[state][action]
        self.q_table[state][action] += self.lr * td_error

def create_game_plot():
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.set_xlim(-0.5, GRID_WIDTH - 0.5)
    ax.set_ylim(-0.5, GRID_HEIGHT - 0.5)
    ax.set_aspect('equal')
    ax.axis('off')
    return fig, ax

def draw_grid(ax):
    for x in range(GRID_WIDTH):
        for y in range(GRID_HEIGHT):
            rect = patches.Rectangle((x-0.5, y-0.5), 1, 1, linewidth=1, edgecolor='gray', facecolor='none')
            ax.add_patch(rect)

def draw_basket(ax, position):
    basket = patches.Rectangle((position-0.4, -0.4), 0.8, 0.8, linewidth=2, edgecolor='blue', facecolor='blue', alpha=0.5)
    return ax.add_patch(basket)

def draw_fruit(ax, position, row):
    fruit = plt.Circle((position, GRID_HEIGHT - 1 - row), 0.3, color='red')
    return ax.add_patch(fruit)

def update(frame, env, agent, ax, basket_patch, fruit_patch, text):
    if frame == 0:
        state = env.reset()
        basket_patch.set_x(state[0] - 0.4)
        fruit_patch.center = (state[1], GRID_HEIGHT - 1)
        text.set_text(f'Episode: {frame // GRID_HEIGHT + 1}, Step: {frame % GRID_HEIGHT + 1}')
        return basket_patch, fruit_patch, text

    state = env.get_state()
    action = agent.get_action(state)
    action_value = ACTIONS[action]
    next_state, reward, done = env.step(action_value)

    basket_patch.set_x(next_state[0] - 0.4)
    fruit_patch.center = (next_state[1], GRID_HEIGHT - 1 - next_state[2])

    agent.update(state, action, reward, next_state)

    text.set_text(f'Episode: {frame // GRID_HEIGHT + 1}, Step: {frame % GRID_HEIGHT + 1}, Reward: {reward}')

    if done:
        env.reset()

    return basket_patch, fruit_patch, text

env = FruitCatchGame()
agent = QLearningAgent(state_space=(GRID_WIDTH, GRID_WIDTH, GRID_HEIGHT), action_space=[0, 1, 2])

fig, ax = create_game_plot()
draw_grid(ax)
basket_patch = draw_basket(ax, env.basket_position)
fruit_patch = draw_fruit(ax, env.fruit_position, env.fruit_row)
text = ax.text(GRID_WIDTH // 2, -1, '', ha='center', va='center', fontsize=12)

anim = animation.FuncAnimation(fig, update, frames=1000, fargs=(env, agent, ax, basket_patch, fruit_patch, text),
                               interval=100, blit=True)

plt.show()