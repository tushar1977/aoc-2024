def func(word_search):
    rows = len(word_search)
    cols = len(word_search[0])
    count = 0
    
    for row in range(1, rows-1): 
        for col in range(1, cols-1):
            if word_search[row][col] == 'A':
                above_left = word_search[row-1][col-1]  
                above_right = word_search[row-1][col+1] 
                below_left = word_search[row+1][col-1] 
                below_right = word_search[row+1][col+1]  
                




                if above_left == 'M' and below_right == 'S' and above_right == 'S' and below_left == 'M':
                    count += 1

                elif above_left == 'S' and below_right == 'M' and above_right == 'S' and below_left == 'M':
                    count += 1

                elif above_left == 'M' and below_right == 'S' and above_right == 'M' and below_left == 'S':
                    count += 1

                elif above_left == 'S' and below_right == 'M' and above_right == 'M' and below_left == 'S':
                    count += 1
                    
    return count






with open("t.txt", 'r') as file:
    word_search = [line.strip() for line in file.readlines()]
result = func(word_search)
print(result)
