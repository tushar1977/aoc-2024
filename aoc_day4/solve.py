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

    direction1 = [(-1, 1), (1, -1), (-1, -1), (1,1), (0,1),(1,0), (0,-1), (-1,0)]
    direction2 = [(-1, -1), (1, 1), (-1, 1), (1, -1)]

    def solve_part_2():

        row = len(grid)
        col = len(grid[0])
        total = 0

        for r in range(row):
            for c in range(col):


                if r < 0 or r  >= row or c <0 or c >= col:
                    continue

                if grid[r][c] == 'A':

                    for dr, dc in direction2:


                        nr, nc = r+dr, c+dc #M 
                        sr, sc = r-dr, c-dc #M
                        br, bc = r+dr, c-dc #S
                        lr, lc = r-dr, c+dc  #S

                        if nr < 0 or nr >= row or nc < 0 or nc >= col:
                            continue
                        if br < 0 or br >= row or bc < 0 or bc >= col:
                            continue
                        if sr < 0 or sr >= row or sc < 0 or sc >= col:
                            continue
                        if lr < 0 or lr >= row or lc < 0 or lc >= col:
                            continue

                        if grid[nr][nc] == 'M' and grid[br][bc] == 'S' and grid[sr][sc] == 'S' and grid[lr][lc] == 'M':
                            total += 1
        print(total)

    def solve_part_1():

        row = len(grid)
        col = len(grid[0])
        total = 0
        target = "XMAS"
        for r in range(row):
            for c in range(col):

                if r < 0 or r  >= row or c <0 or c >= col:
                    continue

                for dr, dc in direction1:

                    found= True
                    for i in range(len(target)):


                        nr, nc = r+i*dr , c+dc*i

                        if(nr < 0 or nr >= row or nc < 0 or nc >= col or grid[nr][nc] != target[i]):
                            found =False
                            break
                    if found:
                        total +=1
                        
        print(total)
    solve_part_1()
    solve_part_2()

solve()
