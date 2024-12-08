from itertools import product

with open("t2.txt", "r") as f:
    raw_data = f.read().splitlines()

final_nums = {}
for line in raw_data:
    key, values = line.split(": ")
    final_nums[int(key)] = list(map(int, values.split(" ")))


def solve2(k, v):
    for combo in product("*+|", repeat=len(v) - 1):
        ans = v[0]
        print(combo)
        for i in range(1, len(v)):
            if combo[i - 1] == "+":
                ans += v[i]
            elif combo[i - 1] == "|":
                ans = int(str(ans) + str(v[i]))
            else:
                ans *= v[i]

        if ans == k:
            return True
    return False


ans2 = 0
for k, v in final_nums.items():
    if solve2(k, v):
        ans2 += k

print("Sum of keys that satisfy the condition:", ans2)
