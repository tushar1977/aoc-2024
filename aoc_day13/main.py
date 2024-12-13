import re


def minimum_tokens(ax, ay, bx, by, px, py):
    px += 10000000000000
    py += 10000000000000

    denominator = ax * by - ay * bx
    if denominator == 0:
        return float("inf")

    i_val = (px * by - py * bx) / denominator
    j_val = (py * ax - px * ay) / denominator

    if i_val.is_integer() and j_val.is_integer() and i_val >= 0 and j_val >= 0:
        return int(3 * i_val + j_val)
    return float("inf")


button_a_list = []
button_b_list = []
prize_list = []

with open("t.txt", "r") as f:
    raw = f.readlines()

for data in raw:
    button_a_coords = re.findall(r"Button A: X\+(\d+), Y\+(\d+)", data)
    button_b_coords = re.findall(r"Button B: X\+(\d+), Y\+(\d+)", data)
    prize_coords = re.findall(r"Prize: X=(\d+), Y=(\d+)", data)

    if button_a_coords:
        button_a_list.extend([(int(x), int(y)) for x, y in button_a_coords])
    if button_b_coords:
        button_b_list.extend([(int(x), int(y)) for x, y in button_b_coords])
    if prize_coords:
        prize_list.extend([(int(x), int(y)) for x, y in prize_coords])
ans = 0
for (ax, ay), (bx, by), (px, py) in zip(button_a_list, button_b_list, prize_list):
    cost = minimum_tokens(ax, ay, bx, by, px, py)
    if cost != float("inf"):
        ans += cost

print(ans)
