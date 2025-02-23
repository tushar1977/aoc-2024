import re

l = []
r = []
with open("t.txt", "r") as f:
    raw = f.read().strip().split("\n")
    for i in raw:
        x, y = i.split("   ")
        l.append(x)
        r.append(y)

print(l)
print(r)
