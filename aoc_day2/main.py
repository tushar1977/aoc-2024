def is_safe(report):
    increasing = all(1 <= report[i + 1] - report[i]<= 3 for i in range(len(report) - 1))
    decreasing = all(1 <= report[i] - report[i + 1]  <= 3 for i in range(len(report) - 1))
    return increasing or decreasing

def remove(report):
    for i in range(len(report)):
        modified = report[:i] + report[i + 1:]
        if is_safe(modified):
            return True

    return False
        


def solve():
    with open('t.txt', 'r') as f:
        reports = [list(map(int, line.split())) for line in f if line.strip()]


    
    safe_count = 0
    safe_count_2 = 0
 
    for report in reports:
        if is_safe(report):
            safe_count_2 = safe_count_2 + 1
        if remove(report):
            safe_count = safe_count + 1
    print(safe_count)
    print(safe_count_2)



solve()
