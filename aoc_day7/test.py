from itertools import product

arr = [20, 3040, 40]
for a in product("*+-", repeat=len(arr) - 1):
    print(a)
