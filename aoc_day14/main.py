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


def divide():
    mid_row = len(grid) // 2
    mid_col = len(grid[0]) // 2

    top_left = [row[:mid_col] for row in grid[:mid_row]]
    top_right = [row[mid_col:] for row in grid[:mid_row]]
    bottom_left = [row[:mid_col] for row in grid[mid_row:]]
    bottom_right = [row[mid_col:] for row in grid[mid_row:]]

    return top_left, top_right, bottom_left, bottom_right


def count_all_numbers(grid_part):
    return sum(row.count("#") for row in grid_part)


def print_grid(grid):
    for row in grid:
        print("".join(row))
    print("\n")


def simulate_robots(robots, t, width, height, grid):
    new_positions = []
    for r in range(height):
        for c in range(width):
            grid[r][c] = "."

    for (x, y), (vx, vy) in robots:
        new_x = (x + vx * t) % width
        new_y = (y + vy * t) % height
        grid[new_y][new_x] = "#"
        new_positions.append((new_x, new_y))
    return new_positions


def part_2(width, height, pos, velocity):
    t = 0
    robots = list(zip(pos, velocity))
    grid = [["." for _ in range(width)] for _ in range(height)]

    while True:
        t += 1
        new_positions = simulate_robots(robots, t, width, height, grid)
        print_grid(grid)

        if len(set(new_positions)) == len(robots):
            break

    print(f"Time taken: {t}")


def part_1():
    robots = list(zip(pos, velocity))

    simulate_robots(robots, time, width, height, grid)

    quan = divide()
    total_counts = [count_all_numbers(part) for part in quan]

    result = 1
    for count in total_counts:
        result *= count
    print(result)


part_2(width, height, pos, velocity)
