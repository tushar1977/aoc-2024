from collections import deque
from itertools import product

directions = {"^": (-1, 0), "v": (1, 0), ">": (0, 1), "<": (0, -1)}

nums = [["7", "8", "9"], ["4", "5", "6"], ["1", "2", "3"], [None, "0", "A"]]


def in_grid(i, j, grid):
    return (0 <= i < len(grid)) and (0 <= j < len(grid[0]))


def bfs(string, grid):
    pos = {}
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            if grid[r][c] is not None:
                pos[grid[r][c]] = (r, c)
    seqs = {}
    print(pos)

    for x in pos:
        for y in pos:
            if x == y:
                seqs[(x, y)] = ["A"]
                continue

            q = deque([(pos[x], "")])
            print(q)
            possibility = []
            optimal = float("inf")

            while q:
                (x, y), moves = q.popleft()

                for nm, (di, dj) in directions.items():
                    new_x, new_y = x + di, y + dj

                    if not in_grid(new_x, new_y, grid) or grid[new_x][new_y] is None:
                        continue

                    if grid[new_x][new_y] == y:
                        if optimal < len(moves) + 1:
                            break
                        optimal = len(moves) + 1
                        possibility.append(moves + nm + "A")
                    else:
                        q.append(((new_x, new_y), moves + nm))
                else:
                    continue
                break
            seqs[(x, y)] = possibility
        op = [seqs[(x, y)] for x, y in zip("A" + string, string)]
        print(list(product(*op)))


bfs("029A", nums)
