import numpy as np
from collections import defaultdict

with open("t.txt") as f:
    grid = np.array([list(line) for line in f.read().splitlines()])

shapex, shapey = np.shape(grid)

neighbour_dict = defaultdict(lambda: set())

for i in range(shapex):
    for j in range(shapey):
        for di, dj in [
            [-1, 0],
            [
                0,
                -1,
            ],
            [0, 1],
            [1, 0],
        ]:
            if i + di in range(shapex) and j + dj in range(shapey):
                if grid[i][j] == grid[i + di][j + dj]:
                    neighbour_dict[(i, j)].add((i + di, j + dj))
print(neighbour_dict)
