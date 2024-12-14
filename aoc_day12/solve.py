from collections import defaultdict


with open("t.txt") as file:
    raw_data = file.readlines()

grid = [data.strip() for data in raw_data]


directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
n = len(grid)

adj4 = [(1, 0), (-1, 0), (0, 1), (0, -1)]
cc = {}


# usinf connected components
def dfs(x, y, curr, i):
    if x in range(n) and y in range(n):
        if (x, y) in cc:
            return
        if grid[x][y] == curr:
            cc[x, y] = i

            for dx, dy in adj4:
                dfs(x + dx, y + dy, curr, i)


for i in range(n):
    for j in range(n):
        if (i, j) not in cc:
            dfs(i, j, grid[i][j], grid[i][j])

ccs = defaultdict(set)

for k, v in cc.items():
    ccs[v].add(k)

print(ccs)
ans = 0
for cc, nodes in ccs.items():
    area = len(nodes)
    peri = 0
    for no in nodes:
        for dx, dy in adj4:
            nx, ny = dx + no[0], dy + no[1]
            if nx not in range(n) or ny not in range(n) or (nx, ny) not in nodes:
                peri += 1
    ans += area * peri
print(ans)
