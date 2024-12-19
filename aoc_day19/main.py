with open("t.txt", "r") as f:
    raw = f.read().strip().split("\n\n")
towels = [p.strip() for p in raw[0].split(",")]
display = [d.strip() for d in raw[1].split("\n")]


def count_ways(display, towels, memo):
    if display in memo:
        return memo[display]

    if display == "":
        return 1

    ways = 0
    for p in towels:
        if display.startswith(p):
            remaining = display[len(p) :]
            ways += count_ways(remaining, towels, memo)

    memo[display] = ways
    return ways


memo = {}


def part_1():
    c = 0
    d = 0
    for d in display:
        if count_ways(d, towels, memo) >= 1:
            c += 1
            total_sum = sum(memo[key] for key in display if key in memo)
            print(total_sum)
    print("part1: ", c)


part_1()
