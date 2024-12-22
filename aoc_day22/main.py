def step(num):
    num = (num ^ (num * 64)) % 16777216
    num = (num ^ (num // 32)) % 16777216
    num = (num ^ (num * 2048)) % 16777216
    return num


seq_total = {}
t = 0

for line in open("t.txt", "r"):
    num = int(line)
    buyer = [num % 10]
    seen = set()
    for _ in range(2000):
        num = step(num)
        buyer.append(num % 10)

    t += num
    for i in range(len(buyer) - 4):
        a, b, c, d, e = buyer[i : i + 5]
        seq = (b - a, c - b, d - c, e - d)
        if seq in seen:
            continue
        if seq not in seq_total:
            seq_total[seq] = 0
        seq_total[seq] += e

print(t)
print(max(seq_total.values()))
