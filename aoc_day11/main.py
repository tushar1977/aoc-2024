with open("t.txt", "r") as f:
    raw = f.read()

stones = [int(num) for num in raw.split() if num.isdigit()]


cache = {}


def part_2(x, n):
    if n == 0:
        return 1

    if (x, n) not in cache:
        if x == 0:
            result = part_2(1, n - 1)
        elif len(str(x)) % 2 == 0:
            x = str(x)
            result = 0
            result += part_2(int(x[: len(x) // 2]), n - 1)
            result += part_2(int(x[len(x) // 2 :]), n - 1)
        else:
            result = part_2(2024 * x, n - 1)
        cache[(x, n)] = result
    return cache[(x, n)]


res = 0
for x in stones:
    # replace with 25
    res += part_2(x, 75)
print(res)
