class GridWorld:
    def __init__(self, size=5, num_obstacles=5, start=(0, 0), goal=(4, 4)):
        self.size = size
        self.start = start
        self.goal = goal
        self.num_obstacles = num_obstacles
        self.obstacles = self._generate_obstacles()
        self.reset()

    def _generate_obstacles(self):
        obstacles = set()
        while len(obstacles) < self.num_obstacles:
            obstacle = (np.random.randint(0, self.size), np.random.randint(0, self.size))
            if obstacle != self.start and obstacle != self.goal:
                obstacles.add(obstacle)
        return list(obstacles)