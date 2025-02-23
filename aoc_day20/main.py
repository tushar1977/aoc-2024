import heapq

with open("t.txt", "r") as f:
    parts = f.read().strip().split("\n\n")
    grid = [list(line) for line in parts[0].split("\n")]

n = len(grid)

directions = [(1, 0), (0, 1), (0, -1), (-1, 0)]

si, sj, ei, ej = 0, 0, 0, 0
for i in range(n):
    for j in range(n):
        if grid[i][j] == "S":
            si, sj = i, j
            grid[i][j] = "."

        if grid[i][j] == "E":
            ei, ej = i, j
            grid[i][j] = "."


def in_grid(i, j):
    return 0 <= i < n and 0 <= j < n


def dikstras(grid, si, sj, ei, ej, max_cheat_time=0):
    pq = [(0, si, sj, 0)]  # cost, row, col, cheat_time
    seen = {(si, sj, 0)}  # Tracks visited states (row, col, cheat_time)
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    while pq:
        cost, r, c, cheat_time = heapq.heappop(pq)
        if (r, c) == (ei, ej):
            return cost

        for dr, dc in directions:
            new_r, new_c = r + dr, c + dc
            new_cheat_time = cheat_time

            if in_grid(new_r, new_c):
                if grid[new_r][new_c] == "#" and cheat_time < max_cheat_time:
                    new_cheat_time += 1  # Use cheat if allowed

                if (grid[new_r][new_c] != "#" or new_cheat_time > cheat_time) and (
                    new_r,
                    new_c,
                    new_cheat_time,
                ) not in seen:
                    seen.add((new_r, new_c, new_cheat_time))
                    heapq.heappush(pq, (cost + 1, new_r, new_c, new_cheat_time))

    return -1


def bfs():
    dist = [[-1] * n for _ in range(n)]
    dist[r][c] = 0


def part1():
    base = dikstras(grid, si, sj, ei, ej)
    cnt = 0
    for i in range(n):
        for j in range(n):
            if grid[i][j] == "#":
                grid[i][j] = "."
                cost = dikstras(grid, si, sj, ei, ej)
                if base - cost >= 100:
                    cnt += 1
                grid[i][j] = "#"

    print(cnt)
