from collections import deque
import heapq
import re


def get_grid(file):
    with open("t.txt", "r") as f:
        parts = f.read().strip().split("\n\n")
        grid = [list(line) for line in parts[0].split("\n")]
    return grid


def get_by_regix():
    with open("t.txt", "r") as f:
        raw = f.readlines()
    for data in raw:
        get_A = re.findall(r"v=(-?\d+),(-?\d+)", data)


directions = [(1, 0), (0, 1), (0, -1), (-1, 0)]

n = 9


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
    print()  # Add a blank line for separation


def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


# A* Algorithm
def a_star(grid, start, goal):
    rows, cols = len(grid), len(grid[0])

    # Priority queue (min-heap)
    open_list = []
    heapq.heappush(open_list, (0, start))

    # Track visited nodes and costs
    g_score = {start: 0}
    f_score = {start: heuristic(start, goal)}
    came_from = {}

    while open_list:
        _, current = heapq.heappop(open_list)

        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1]  # Return reconstructed path

        x, y = current

        # Explore neighbors
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            neighbor = (x + dx, y + dy)

            if not (0 <= neighbor[0] < rows and 0 <= neighbor[1] < cols):
                continue  # Out of bounds
            if grid[neighbor[0]][neighbor[1]] == 0:
                continue  # Blocked cell

            tentative_g_score = g_score[current] + 1

            if tentative_g_score < g_score.get(neighbor, float("inf")):
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + heuristic(neighbor, goal)
                heapq.heappush(open_list, (f_score[neighbor], neighbor))

    return None  # No path found
