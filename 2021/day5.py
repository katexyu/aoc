from collections import defaultdict
from math import floor

def solve(coordinates):
    candidates = list(filter(lambda x: isvalid(x), coordinates))
    print(f'coords: {len(coordinates)}, candidates: {len(candidates)}')
    
    grid = []
    for i in range(1000):
        row = []
        for j in range(1000):
            row.append(0)
        grid.append(row)
    
    for c in candidates:
        c1 = c[0]
        c2 = c[1]
        if c1[0] == c2[0]:
            lo = min(c1[1], c2[1])
            hi = max(c1[1], c2[1])
            x = c1[0]

            # fill in horizontally
            for i in range(lo, hi + 1):
                grid[x][i] += 1
                
        elif c1[1] == c2[1]:
            lo = min(c1[0], c2[0])
            hi = max(c1[0], c2[0])
            y = c1[1]

            # fill in vertically
            for j in range(lo, hi+1):
                grid[j][y] += 1

    num_points = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] >= 2:
                num_points += 1
    return num_points


def solveb(candidates):
    grid = []
    for i in range(1000*1000):
        grid.append(0)

    for c1, c2 in candidates:
        # fill in diagonally
        xstep = sign(c2[0] - c1[0])
        ystep = sign(c2[1] - c1[1])
        print(f'Filling in diagonally c1: {c1} c2: {c2}, xstep: {xstep}, ystep: {ystep}')
           
        x, y = c1 
        while True:
            grid[x*1000+y] += 1
            x += xstep
            y += ystep      
            if x == c2[0] and y == c2[1]:
                break      
        grid[x*1000+y] += 1

    num_points = 0
    for val in grid:
        if val > 1:
            num_points += 1
    return num_points


def isvalid(pair):
    c1 = pair[0]
    c2 = pair[1]
    return c1[0] == c2[0] or c1[1] == c2[1]    


def sign(a):
    return (a > 0) - (a < 0)
   
 
def get_data(filename='day5.txt'):
    coordinates = []
    with open(filename, 'r') as f:
        lines = f.readlines()
        for l in lines:
            parts = l.split('->')
            c1 = [int(i) for i in parts[0].strip(' ').split(',')]
            c2 = [int(i) for i in parts[1].strip(' ').split(',')]
            coordinates.append([c1, c2])
        
    return coordinates


if __name__=='__main__':
    coordinates = get_data()

    print(solve(coordinates))
    print(solveb(coordinates))
