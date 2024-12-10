with open("t.txt", "r") as f:
    raw = f.read().splitlines()

grid = [list(map(int, line.strip())) for line in raw]
rows, cols = len(grid), len(grid[0])
path_count = 0


def solve(visited, i, j):
    global path_count
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    if grid[i][j] == 9:
        path_count = path_count + 1
        return

    for di, dj in directions:
        ni, nj = i + di, j + dj

        if 0 <= ni < rows and 0 <= nj < cols and (ni, nj) not in visited:
            if grid[ni][nj] == grid[i][j] + 1:
                visited.add((ni, nj))
                solve(visited, ni, nj)
                visited.remove((ni, nj))


total_paths = 0
for i in range(rows):
    for j in range(cols):
        if grid[i][j] == 0:
            solve({(i, j)}, i, j)

print(path_count)
