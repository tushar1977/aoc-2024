with open("t.txt", "r") as f:
    raw = f.read().splitlines()

grid = [list(map(int, line.strip())) for line in raw]
rows, cols = len(grid), len(grid[0])
print(grid)
directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]


def in_grid(i, j):
    return (0 <= i < rows) and (0 <= j < cols)


def bfs(i, j):
    if grid[i][j] != 0:
        return 0

    ans = 0

    stack = [(i, j)]
    visited = set()
    while len(stack) > 0:
        curi, curj = stack.pop()
        curr = int(grid[curi][curj])

        if (curi, curj) in visited:
            continue
        visited.add((curi, curj))

        if curr == 9:
            ans += 1
            continue
        for di, dj in directions:
            ni, nj = curi + di, curj + dj

            if not in_grid(ni, nj):
                continue
            next = int(grid[ni][nj])
            if next != curr + 1:
                continue

            stack.append((ni, nj))
    return ans


total = 0
for i in range(rows):
    for j in range(cols):
        total += bfs(i, j)


print(total)
