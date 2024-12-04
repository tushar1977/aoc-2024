

import numpy as np

def solve():
    with open('t.txt', 'r') as f:
        lines = f.readlines()
        row = len(lines)
        word = "".join([line.strip() for line in lines])
    
    l = [ch for ch in word]  
    arr = np.array(l)
    col = len(lines[0].strip()) 

    grid = arr.reshape(row, col)

    t = 0
    for r in range(row):
        for c in range(col):
            if grid[r][c] == "A":  
                criss = False
                for dr in [-1,1]:
                    for dc in [-1,1]:
                    

                        if (
                            0 <= r+dr < row and 0 <= c+dc < col and
                            grid[r+dr][c+dc] == "M") :
                                a,b = r-dr, c-dc

                                if(a >= len(grid) or a <0 or b >= len (grid[0]) or b < 0):
                                    continue
                                
                                if grid[a][b] == 'S':
                                    if not criss:
                                        criss = True
                                    else:
                                        t+=1


                        
    print(t)





    
solve()
        
