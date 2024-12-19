with open("t.txt", 'r') as f:
    parts = f.read().strip().split("\n\n")
    grid = [list(line) for line in parts[0].split("\n")]
    steps = parts[1].replace("\n", "")


n = len(grid)

boxes = []
walls = []

dirs = {
    "<": [0,-1],
    ">": [0,1],
    "v":[1,0],
    "^":[-1,0]
}

for i in range(n):
    for j in range(n):
        if grid[i][j] == "@":
            ci, cj = i, j
            break

def in_grid(i, j):
    return (0<=i<n) and (0<=j<n)

def solve(dir):
    global ci, cj, grid

    new_i, new_j = ci+dir[0] , cj+dir[1]
    if not in_grid(new_i, new_j):
        return

    di , dj = ci, cj
    while in_grid(di, dj):
        di += dir[0]
        dj += dir[1]

        if grid[di][dj] == "#":
            break

        if grid[di][dj] == ".":
            grid[di][dj] = "O"
            grid[ci][cj] = "."
            ci, cj = ci+dir[0], cj+dir[1] 
            grid[ci][cj] = "@"
            break
for m in steps:
    solve(dirs[m])

ans = 0
for i in range(n):
    for j in range(n):
        if grid[i][j] == "O":
            ans += 100*i+j
print(ans)

for i in range(n):
    for j in range(n):
        if grid[i][j] == "@":
            ci, cj = i, j*2
        elif grid[i][j] == "O":
            boxes.append([i, j*2])
            boxes.append([i, j*2+1])
        elif grid[i][j] == "#":
            walls.append([i, j*2])
            walls.append([i, j*2+1])

def move(dir):
    global ci, cj, grid

    newi, newj = ci+dir[0] , cj+dir[1]

    if not in_grid(newi, newj):
        return

    if [newi, newj] in walls:
        return

    stack = []

    if [newi, newj] in boxes:
        stack.append([newi, newj])
    if [newi, newj-1] in boxes:

        stack.append([newi, newj-1])

    can_move = True

    seen = set()
    while len(stack) > 0:

        topi, topj = stack.pop()
        ni , nj = topi + dir[0], topj + dir[1]

        if not in_grid(ni, nj):
            can_move=False
            break
        if [ni, nj] or [ni, nj+1]  in walls:
            can_move = False
            break
        if (topi, topj) in seen:
            continue
        seen.add((topi, topj))

        if [ni, nj] in boxes:
            stack.append([ni, nj])

        if [ni, nj+1] in boxes:
            stack.append([ni, nj+1])

        if [ni, nj-1] in boxes:
            stack.append([ni, nj-1])
    if not can_move:
        return 

