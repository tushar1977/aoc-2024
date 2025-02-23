grid = [list(line.strip()) for line in open("t.txt", "r")]

rows = len(grid)
cols = rows

r, c = 0, 0
for r in range(rows):
    for c in range(cols):
        if grid[r][c] == "S":
            r, c = r, c
            break
    else:
        continue

    break

dists = [[-1] * cols for _ in range(rows)]
dists[r][c] = 0

while grid[r][c] != "E":
    for nr, nc in [(r + 1, c), (r, c + 1), (r - 1, c), (r, c - 1)]:
        if nr < 0 and nc < 0 and nr >= rows and nc >= cols:
            continue
        if grid[nr][nc] == "#":
            continue

        dists[nr][nc] = dists[r][c] + 1
        r = nr
        c = nc


for r in range(rows):
    for c in range(cols):
        if grid[r][c] == "#":
            continue
        if r < 0 and c < 0 and r >= rows and c >= cols:
            continue

        if abs(dist[r][c] - dist[nr][nc])
