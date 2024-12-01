def solve():
    with open("t.txt", 'r') as f:
        num = list(map(int, f.read().split()))
        
        l1 = [num[i] for i in range(len(num)) if i % 2 == 0]
        l2 = [num[i] for i in range(len(num)) if i % 2 == 1]
        
        l1.sort()
        l2.sort()

        cnt = 0

        for i in range(0, len(l1)):

            cnt += l1[i]*l2.count(l1[i])


        print("Total Count", cnt)

def solve2():

    with open("t.txt", 'r') as f:
        num = list(map(int, f.read().split()))
        
        l1 = [num[i] for i in range(len(num)) if i % 2 == 0]
        l2 = [num[i] for i in range(len(num)) if i % 2 == 1]
        
        l1.sort()
        l2.sort()

        total_distance = sum(abs(l1[i] - l2[i]) for i in range(min(len(l1), len(l2))))
        
        print("Total distance:", total_distance)


        
        

        
solve()
solve2()
