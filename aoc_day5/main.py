def solve():
    with open("t.txt") as f:
        lines = f.read().splitlines()

    print(lines)
    rules = []
    cnt = 0
    cnt2 = 0
    updates = []
    parsing_rules = True

    for line in lines:
        if line == "":
            parsing_rules = False
            continue
        if parsing_rules:
            rules.append(list(map(int, line.split("|"))))
        else:
            updates.append(list(map(int, line.split(","))))
    print(rules)
    print(updates)


    def is_update_valid(update):
        is_valid = True  
        swapped = True 
        while swapped:  
            swapped = False
            for A, B in rules:
                if A in update and B in update:
                    page1_idx = update.index(A)
                    page2_idx = update.index(B)
                    if page1_idx > page2_idx:  
                        update[page1_idx], update[page2_idx] = update[page2_idx], update[page1_idx]
                        swapped = True  
                        is_valid = False  
        return is_valid


    cnt = 0
    cnt2 = 0

    for _, update in enumerate(updates):
        if is_update_valid(update): 
            cnt += update[len(update) // 2]  
        else: 
            cnt2 += update[len(update) // 2]  

    print( cnt)
    print( cnt2)

solve()
