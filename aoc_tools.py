from collections import deque
import heapq
import re


with open("t.txt", "r") as f:
    parts = f.read().strip().split("\n\n")
    grid = [list(line) for line in parts[0].split("\n")]


def get_by_regix():
    with open("t.txt", "r") as f:
        raw = f.readlines()
    for data in raw:
        get_A = re.findall(r"v=(-?\d+),(-?\d+)", data)


directions = [(1, 0), (0, 1), (0, -1), (-1, 0)]


def in_grid(i, j):
    return (0 <= i < n) and (0 <= j < n)


def bfs(i, j):
    seen = set()

    Q = deque((i, j))
    while len(Q) > 0:
        for ni, ny in directions:
            new_x, new_y = i + ni, j + ny

            if not in_grid(new_x, new_y) or (new_x, new_y) not in seen:
                return
            seen.add((new_x, new_y))


def dfs(grid, x, y, visited):
    if not in_grid(x, y) or (x, y) in visited or grid[x][y] == "#":
        return

    visited.add((x, y))
    print(f"{x},{y} visited")

    for di, dj in directions:
        dfs(grid, x + di, y + dj, visited)


def dikstras(grid, ei, ej):
    pq = [(0, 0, 0)]
    seen = {(0, 0)}
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    while pq:
        cost, r, c = heapq.heappop(pq)
        if (r, c) == (ei, ej):
            return True, cost

        for dr, dc in directions:
            new_r, new_c = r + dr, c + dc
            if (
                in_grid(new_r, new_c)
                and grid[new_r][new_c] != "#"
                and (new_r, new_c) not in seen
            ):
                seen.add((new_r, new_c))
                heapq.heappush(pq, (cost + 1, new_r, new_c))

    return False, -1


def print_grid(grid):
    for row in grid:
        print("".join(row))
    print()


def dp_memo(display, towels, memo):
    if display in memo:
        return memo[display]

    if display == "":
        return 1

    ways = 0
    for p in towels:
        if display.startswith(p):
            remaining = display[len(p) :]
            ways += dp_memo(remaining, towels, memo)

    memo[display] = ways
    return ways
