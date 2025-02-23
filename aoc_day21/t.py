from pathlib import Path
from functools import cache


def parse(input: str) -> list[tuple[str, int]]:
    return [(line, int(line[:-1], 10)) for line in input.splitlines()]


NUMERIC = {
    "7": (0, 0),
    "8": (0, 1),
    "9": (0, 2),
    "4": (1, 0),
    "5": (1, 1),
    "6": (1, 2),
    "1": (2, 0),
    "2": (2, 1),
    "3": (2, 2),
    "0": (3, 1),
    "A": (3, 2),
}
DIRECTIONS = {"^": (0, 1), "A": (0, 2), "<": (1, 0), "v": (1, 1), ">": (1, 2)}


@cache
def numeric_pad(current: str, want: str) -> list[str]:
    """Returns a list of the shortest routes between the two keys."""
    cur_y, cur_x = NUMERIC[current]
    want_y, want_x = NUMERIC[want]
    routes = []
    moves = [("", cur_x, cur_y)]
    while moves:
        m = moves
        moves = []
        for d, x, y in m:
            if want_x < x:
                if y != 3 or x != 1:
                    moves.append((d + "<", x - 1, y))
            elif want_x > x:
                moves.append((d + ">", x + 1, y))
            if want_y < y:
                moves.append((d + "^", x, y - 1))
            elif want_y > y:
                if y != 2 or x != 0:
                    moves.append((d + "v", x, y + 1))
            elif want_x == x and want_y == y:
                routes.append(d)
    print([r + "A" for r in routes if r])
    return [r + "A" for r in routes if r]


@cache
def direction_pad(current: str, want: str) -> list[str]:
    """Returns a list of the shortest routes between the two keys."""
    cur_y, cur_x = DIRECTIONS[current]
    want_y, want_x = DIRECTIONS[want]
    routes = []
    moves = [("", cur_x, cur_y)]
    while moves:
        m = moves
        moves = []
        for d, x, y in m:
            if want_x < x:
                if y != 0 or x != 1:
                    moves.append((d + "<", x - 1, y))
            elif want_x > x:
                moves.append((d + ">", x + 1, y))
            if want_y < y:
                if x != 0:
                    moves.append((d + "^", x, y - 1))
            elif want_y > y:
                moves.append((d + "v", x, y + 1))
            elif want_x == x and want_y == y:
                routes.append(d)
    print("direction", [r + "A" for r in routes])
    return [r + "A" for r in routes]


@cache
def cost_for_direction_pair(p2a: str, p2b: str) -> int:
    cur_y, cur_x = DIRECTIONS[p2a]
    want_y, want_x = DIRECTIONS[p2b]
    return abs(cur_y - want_y) + abs(cur_x - want_x) + 1


@cache
def cost_forpadseq(seq: str, npads: int) -> int:
    res = sum(padcost(p2a, p2b, npads) for p2a, p2b in zip("A" + seq, seq))
    return res


def padcost(c0: str, c1: str, npads: int) -> int:
    if npads == 1:
        return cost_for_direction_pair(c0, c1)
    return min(cost_forpadseq(seq, npads - 1) for seq in direction_pad(c0, c1))


@cache
def humancost(seq: str, npads: int = 3) -> int:
    res = sum(padcost(p2a, p2b) for p2a, p2b in zip("A" + seq, seq))
    return res


@cache
def humanpad(c0: str, c1: str, npads: int) -> int:
    costs = []
    for pad1_route in numeric_pad(c0, c1):
        costs.append(cost_forpadseq(pad1_route, npads - 1))
    return min(costs)


def enter_code2(code: str, npads: int) -> int:
    cost = sum(humanpad(c0, c1, npads) for c0, c1 in zip("A" + code[:-1], code))
    return cost


def part2(codes: list[tuple[str, int]], npads: int = 3) -> int:
    return sum(value * enter_code2(code, npads) for code, value in codes)


TEST = parse(Path("t.txt").read_text())
INPUT = parse(Path("t.txt").read_text())
part1_total = part2(INPUT, 3)
print(f"{part1_total=:,}")  # 164,960

part2_total = part2(INPUT, 26)
print(f"{part2_total=:,}")  # 205,620,604,017,764
