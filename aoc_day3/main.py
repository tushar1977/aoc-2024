import re

def solve():
    with open("t.txt", 'r') as f:
        word = f.read().split()
        pattern = r"mul\((\d+),(\d+)\)"

        t = 0
        
        for w in word:
            matches = re.findall(pattern, w)
            for m in matches:
                x, y = map(int, m)
                t+= x*y
        print(t)

def solve2():

    with open("t.txt") as file:
        raw_data = file.read()


    pattern = r"(do|don't)\(\)|mul\((\d+),(\d+)\)"

    matches = re.findall(pattern, raw_data)


    result = 0
    do = True
    for match in matches:
        condition, num1, num2 = match
        if condition == "do":
            do = True
        elif condition == "don't":
            do = False
        else:
            if do: result += int(num1) * int(num2)

    print(result)
