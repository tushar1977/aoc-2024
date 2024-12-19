from collections import defaultdict, deque
import heapq
from os import cpu_count
import sys

sys.setrecursionlimit(10000)

with open("t.txt", "r") as f:
    parts = f.read().strip().split("\n\n")
    grid = [list(line) for line in parts[0].split("\n")]

n = len(grid)
m = len(grid[0])

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
si, sj, ei, ej = 0, 0, 0, 0

for i in range(n):
    for j in range(m):
        if grid[i][j] == "S":
            si, sj = i, j
        if grid[i][j] == "E":
            ei, ej = i, j


def in_grid(i, j):
    return 0 <= i < n and 0 <= j < m


def part_1():
    pq = [
        (
            0,
            si,
            sj,
            0,
        )
    ]
    seen = {(si, sj, 0)}

    while pq:
        cost, r, c, d = heapq.heappop(pq)
        if (r, c) == (ei, ej):
            print(cost)

        new_r, new_c = r + directions[d][0], c + directions[d][1]
        if (
            in_grid(new_r, new_c)
            and grid[new_r][new_c] != "#"
            and (new_r, new_c, d) not in seen
        ):
            seen.add((new_r, new_c, d))
            heapq.heappush(pq, (cost + 1, new_r, new_c, d))

        for turn_cost, new_d in [(1000, (d - 1) % 4), (1000, (d + 1) % 4)]:
            if (r, c, new_d) not in seen:
                seen.add((r, c, new_d))


def part_2():
    routes = []
    visited = {}
    start = (si, sj)
    queue = [(start, [start], 0, 0)]

    while queue:
        (x, y), history, curr_score, curr_dir = queue.pop(0)
        if (x, y) == (ei, ej):
            routes.append((history, curr_score))

            continue

        if ((x, y), curr_dir) in visited and visited[((x, y), curr_dir)] < curr_score:
            continue

        visited[((x, y), curr_dir)] = curr_score

        for d, (di, dy) in enumerate(directions):
            if (curr_dir + 2) % 4 == d:
                continue

            nx, ny = x + di, y + dy

            if grid[nx][ny] != "#" and (nx, ny) not in history:
                if d == curr_dir:
                    queue.append(((nx, ny), history + [(nx, ny)], curr_score + 1, d))
                else:
                    queue.append(((nx, ny), history + [(nx, ny)], curr_score + 1000, d))

    for i in routes:
        print(i)


part_2()
