with open("t.txt") as file:
    raw_data = file.readlines()

map = []
for data in raw_data:
    map.append(data.strip())

pos = []
obs_dict = {}
print(map)
for y, row in enumerate(map):
    for x, obj in enumerate(row):
        if obj == "#":
            obs_dict[f"{x},{y}"] = True
        if obj == "^":
            pos = [x, y]

print(map[1][1])
directions = [[0, -1], [1, 0], [0, 1], [-1, 0]]
curr_dir = 0
visited = set()

while 0 < pos[0] < len(map[0]) and 0 < pos[1] < len(map):
    direction = directions[curr_dir]

    print("current dir", direction)
    new_pos = [pos[0] + direction[0], pos[1] + direction[1]]
    print("new pos", new_pos)

    if obs_dict.get(f"{new_pos[0]},{new_pos[1]}"):
        curr_dir += 1
        curr_dir %= len(directions)
    else:
        visited.add(f"{new_pos[0]},{new_pos[1]}")
        pos = new_pos

print(len(visited))
