g = {}

start = None
exit = None
for y, line in enumerate(open("t.txt").readlines()):
    for x, c in enumerate(line.strip()):
        g[(x, y)] = c
        if c == "S":
            start = (x, y)
        if c == "E":
            exit = (x, y)

best = 100000
paths = set()
q = [(start, (1, 0), set([]), 0)]
seen = {}
while len(q):
    pos, dir, path, score = q.pop(0)
    if (pos, dir) in seen:
        if seen[(pos, dir)] < score:
            continue
    seen[(pos, dir)] = score

    if pos == exit:
        if score < best:
            best = score
            paths.clear()
            paths.update(path)
        elif score == best:
            paths.update(path)
        continue

    nx, ny = pos[0] + dir[0], pos[1] + dir[1]
    if (nx, ny) in g and g[(nx, ny)] != "#":
        q.append(((nx, ny), dir, path.union([pos]), score + 1))
    # turn left
    q.append((pos, (dir[1], -dir[0]), path, score + 1000))
    # turn right
    q.append((pos, (-dir[1], dir[0]), path, score + 1000))

# smallest score
print(min(seen[(pos, dir)] for (pos, dir) in seen if pos == exit))
# number of spaces along best paths
print(len(paths) + 1)  # +1 for exit
