from collections import deque

# Directions for all 8 possible moves (up, down, left, right, diagonals)
directions = [(-1, 0), (0, -1), (1, 0), (0, 1), (1, 1), (1, -1), (-1, 1), (-1, -1)]

# Function to read the grid from a file
def read_grid_from_file(filename):
    with open(filename, 'r') as f:
        return [list(line.strip()) for line in f.readlines()]

def bfs(start, goal, n, grid):
    queue = deque([(start[0], start[1], 0)])  # (i, j, distance)
    visited = set()
    visited.add(start)
    parent = {}  # To track the path
    found = False

    while queue and not found:
        i, j, dist = queue.popleft()

        for ni, nj in directions:
            new_i, new_j = i + ni, j + nj
            if 0 <= new_i < n and 0 <= new_j < n and (new_i, new_j) not in visited:
                if grid[new_i][new_j] == "#":  # Valid position
                    parent[(new_i, new_j)] = (i, j)  # Record the parent node
                    visited.add((new_i, new_j))

                    if (new_i, new_j) == goal:
                        found = True
                        break

                    queue.append((new_i, new_j, dist + 1))
    if found:
        path = []
        current = goal
        while current != start:
            path.append(current)
            current = parent[current]
        path.append(start)
        path.reverse()

        for idx, (i, j) in enumerate(path):
            if grid[i][j] == "#":
                grid[i][j] = str(idx + 1)
        print(path)
        
# Main function
def main(filename):
    grid = read_grid_from_file(filename)
    n = len(grid)  # Size of the grid

    start = None
    goal = None

    for i in range(n):
        for j in range(n):
            if grid[i][j] == "#" and start is None:
                start = (i, j)  # First # as start
            if grid[i][j] == "#":
                goal = (i, j)  # Last # as goal

    print(start, goal)
    bfs(start, goal, n, grid)
    for row in grid:
        print("".join(row))

filename = "t.txt"  # Ensure the file is in the same directory or provide a full path

main(filename)
