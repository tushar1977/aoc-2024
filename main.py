with open("t.txt", "r") as f:
    raw = f.read().strip()

hail = {}
print(raw)
n = 0
for line in raw:
    pos = []
    vec = []
