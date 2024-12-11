with open("t.txt", "r") as f:
    raw = f.read()

stones = [int(num) for num in raw.split() if num.isdigit()]

new_l = []

i = 0


def process_stone(stone, memo):
    if stone in memo:
        return memo[stone]

    if stone == 0:
        result = [1]
    elif len(str(stone)) % 2 == 0:
        digits = str(stone)
        mid = len(digits) // 2
        first_half = digits[:mid]
        second_half = digits[mid:]

        result = [int(first_half)]
        if set(second_half) == {"0"}:
            result.append(0)
        else:
            result2 = second_half.lstrip("0")
            result.append(int(result2))
    else:
        result = [stone * 2024]

    memo[stone] = result
    return result


memo = {}
i = 0
while i < 25:
    new_l = []
    for stone in stones:
        new_l.extend(process_stone(stone, memo))
    stones = new_l
    print(i)
    i += 1


print(len(new_l))
