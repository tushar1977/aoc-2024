import heapq

with open("t.txt", "r") as f:
    raw = f.readlines()

row, col = 71, 71
e = 70

pos = []
for line in raw:
    x, y = map(int, line.strip().split(","))
    pos.append((x, y))


def in_grid(i, j):
    return 0 <= i < row and 0 <= j < col


def is_path(grid):
    pq = [(0, 0, 0)]
    seen = {(0, 0)}
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    while pq:
        cost, r, c = heapq.heappop(pq)
        if (r, c) == (e, e):
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


# part 1
grid_1 = [["." for _ in range(col)] for _ in range(row)]

for c, r in pos:
    grid_1[r][c] = "#"
is_path(grid_1)

grid = [["." for _ in range(col)] for _ in range(row)]

# Part 2
for c, r in pos:
    grid[r][c] = "#"
    if not is_path(grid):
        print(f"{c},{r}")
        break
