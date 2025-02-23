locks = []
keys = []


with open("t.txt", "r") as f:
    parts = f.read().strip()
    for i in parts.split("\n\n"):
        grid2 = [j for j in i.split("\n")]
        isl = False

        if grid2[0] == "#####":
            isl = True

        hts = [
            sum(1 for i in range(len(grid2)) if grid2[i][j] == "#") - 1
            for j in range(len(grid2[0]))
        ]

        if isl:
            locks.append(tuple(hts))
        else:
            keys.append(tuple(hts))

# print(locks)
# print(keys)
t = 0
for lock in locks:
    for key in keys:
        if all(a + b <= 5 for a, b in zip(lock, key)):
            t += 1

print("Total Compatible Pairs:", t)
