import re

with open("t.txt", "r") as f:
    raw = f.readlines()
pos = []
velocity = []
for data in raw:
    position_coords = re.findall(r"p=(-?\d+),(-?\d+)", data)
    velocity_coords = re.findall(r"v=(-?\d+),(-?\d+)", data)

    pos.extend([(int(x), int(y)) for x, y in position_coords])
    velocity.extend([(int(x), int(y)) for x, y in velocity_coords])

width, height = 101, 103
time = 100

grid = [["." for _ in range(width)] for _ in range(height)]


def simulate_robots(robots, t):
    new_positions = []
    for (x, y), (vx, vy) in robots:
        new_x = (x + vx * t) % width
        new_y = (y + vy * t) % height
        new_positions.append((new_x, new_y))
    return new_positions


def part_2():
    t = 0
    tree = []
    robots = list(zip(pos, velocity))
    while True:
        t += 1
        new_positions = simulate_robots(robots, t)

        grid = [["." for _ in range(width)] for _ in range(height)]

        for x, y in new_positions:
            grid[y][x] = "#"

        if len(set(new_positions)) == len(robots):
            for row in grid:
                print("".join(row))

            print(t)
            break


part_2()
