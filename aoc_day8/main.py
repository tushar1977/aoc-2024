from itertools import combinations
import math

with open("t.txt", "r") as f:
    raw = f.read().splitlines()


grid = []

for data in raw:
    grid.append(data.strip())

freq = []
print(grid)
for i in range(len(grid)):
    for j in range(len(grid)):
        if grid[i][j].isalnum():
            freq.append((grid[i][j], i, j))

antinodes = set()


def get_anti(x, y):
    _, ax, ay = x
    _, bx, by = y

    new_ax, new_ay = ax - (bx - ax), ay - (by - ay)
    new_bx, new_by = bx + (bx - ax), by + (by - ay)

    if 0 <= new_ax < len(grid) and 0 <= new_ay < len(grid):
        antinodes.add((new_ax, new_ay))

    if 0 <= new_bx < len(grid) and 0 <= new_by < len(grid):
        antinodes.add((new_bx, new_by))


print(freq)
for i in range(len(freq)):
    for j in range(i + 1, len(freq)):
        a = freq[i]
        b = freq[j]

        if a[0] == b[0]:
            get_anti(a, b)

print(antinodes)
print(len(antinodes))
