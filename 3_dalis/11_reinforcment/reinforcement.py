import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.animation as animation

# Set the grid size
GRID_SIZE = (3, 4)  # (rows, columns)

class GridWorld:
    def __init__(self, size):
        self.size = size
        self.grid = np.zeros(size)
        self.grid[size[0]//2, size[1]//2] = -1  # Obstacle
        self.grid[0, size[1]-1] = 1   # Goal
        self.state = (size[0]-1, 0)   # Start state
        self.actions = [(0, 1), (0, -1), (-1, 0), (1, 0)]  # Right, Left, Up, Down

    def reset(self):
        self.state = (self.size[0]-1, 0)
        return self.state

    def step(self, action):
        new_state = (
            max(0, min(self.size[0]-1, self.state[0] + action[0])),
            max(0, min(self.size[1]-1, self.state[1] + action[1]))
        )
        reward = self.grid[new_state]
        done = reward != 0
        self.state = new_state
        return new_state, reward, done

class QLearningAgent:
    def __init__(self, state_size, action_size, learning_rate=0.1, discount_factor=0.9, epsilon=0.1):
        self.q_table = np.zeros(state_size + (action_size,))
        self.lr = learning_rate
        self.gamma = discount_factor
        self.epsilon = epsilon

    def get_action(self, state):
        if np.random.random() < self.epsilon:
            return np.random.randint(4)
        return np.argmax(self.q_table[state])

    def update(self, state, action, reward, next_state):
        best_next_action = np.argmax(self.q_table[next_state])
        td_target = reward + self.gamma * self.q_table[next_state][best_next_action]
        td_error = td_target - self.q_table[state][action]
        self.q_table[state][action] += self.lr * td_error

def create_grid_world_plot(size):
    fig, ax = plt.subplots(figsize=(12, 10))
    ax.set_xlim(-0.5, size[1]-0.5)
    ax.set_ylim(-0.5, size[0]-0.5)
    ax.set_aspect('equal')
    ax.axis('off')
    return fig, ax

def draw_grid(ax, size):
    for x in range(size[1]):
        for y in range(size[0]):
            rect = patches.Rectangle((x-0.5, y-0.5), 1, 1, linewidth=1, edgecolor='gray', facecolor='none')
            ax.add_patch(rect)

def draw_obstacle(ax, size):
    obstacle = patches.Rectangle((size[1]//2-0.5, size[0]//2-0.5), 1, 1, linewidth=2, edgecolor='black', facecolor='red', alpha=0.3)
    ax.add_patch(obstacle)

def draw_goal(ax, size):
    goal = patches.Rectangle((size[1]-1.5, size[0]-1.5), 1, 1, linewidth=2, edgecolor='black', facecolor='green', alpha=0.3)
    ax.add_patch(goal)

def draw_agent(ax, state):
    agent = plt.Circle((state[1], size[0]-1-state[0]), 0.3, color='blue')
    return ax.add_patch(agent)

def draw_q_values(ax, q_table, size, texts):
    for txt in texts:
        txt.remove()
    texts.clear()
    for i in range(size[0]):
        for j in range(size[1]):
            for k, (di, dj) in enumerate([(0.25, 0), (-0.25, 0), (0, 0.25), (0, -0.25)]):
                text = ax.text(j+di, size[0]-1-i+dj, f'{q_table[i,j,k]:.1f}', ha='center', va='center', fontsize=6, color='black', bbox=dict(facecolor='white', alpha=0.7, edgecolor='none'))
                texts.append(text)

def update(frame, env, agent, ax, agent_patch, text, reward_text, q_values_texts, cumulative_rewards, episode_rewards):
    if frame % 20 == 0:
        state = env.reset()
        if episode_rewards:
            cumulative_rewards.append(sum(episode_rewards))
        episode_rewards.clear()
        agent_patch.center = (state[1], size[0]-1-state[0])
        draw_q_values(ax, agent.q_table, size, q_values_texts)
        text.set_text(f'Episode: {frame // 20 + 1}, Step: 1')
        reward_text.set_text(f'Cumulative Reward: {cumulative_rewards[-1] if cumulative_rewards else 0}')
    else:
        text.set_text(f'Episode: {frame // 20 + 1}, Step: {frame % 20 + 1}')
        
    state = env.state
    action = agent.get_action(state)
    next_state, reward, done = env.step(env.actions[action])
    agent.update(state, action, reward, next_state)
    episode_rewards.append(reward)

    agent_patch.center = (next_state[1], size[0]-1-next_state[0])

    # Redraw Q-values every 5 steps
    if frame % 5 == 0:
        draw_q_values(ax, agent.q_table, size, q_values_texts)

    if done:
        env.reset()

    return agent_patch, text, reward_text

size = GRID_SIZE
env = GridWorld(size)
agent = QLearningAgent(size, 4)

fig, ax = create_grid_world_plot(size)
draw_grid(ax, size)
draw_obstacle(ax, size)
draw_goal(ax, size)
agent_patch = draw_agent(ax, env.state)
text = ax.text(size[1]//2, -0.7, '', ha='center', va='center', fontsize=12)
reward_text = ax.text(size[1]//2, -1.0, '', ha='center', va='center', fontsize=12)
q_values_texts = []

cumulative_rewards = []
episode_rewards = []

anim = animation.FuncAnimation(fig, update, frames=1000, fargs=(env, agent, ax, agent_patch, text, reward_text, q_values_texts, cumulative_rewards, episode_rewards),
                               interval=100, blit=False)

plt.show()
