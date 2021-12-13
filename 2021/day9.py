from helpers import parse_digits_grid


def solve(data):
    l = len(data)
    h = len(data[0])

    s = 0
    
    for i in range(l):
        for j in range(h):
            low = True
            val = data[i][j]
            if i > 0 and data[i-1][j] <= val:
                low = False
            if i < l-1 and data[i+1][j] <= val:
                low = False
            if j > 0 and data[i][j-1] <= val:
                low = False
            if j < h-1 and data[i][j+1] <= val:
                low = False
            if low:
                s += 1+val
    return s        


def solveb(data):
    l = len(data)
    h = len(data[0])

    low_points = []
    
    for i in range(l):
        for j in range(h):
            low = True
            val = data[i][j]
            if i > 0 and data[i-1][j] <= val:
                low = False
            if i < l-1 and data[i+1][j] <= val:
                low = False
            if j > 0 and data[i][j-1] <= val:
                low = False
            if j < h-1 and data[i][j+1] <= val:
                low = False
            if low:
                low_points.append((i, j))

    sizes = []

    for i,j in low_points:
       size = find_basin_size(i, j, data)
       sizes.append(size)
    
    sizes.sort()
    sizes.reverse()
    return sizes[0] * sizes[1] * sizes[2] 


def find_basin_size(ii, jj, data):
    visited = set()
    q = [(ii, jj)]
    visited.add((ii,jj))
    l = len(data)
    h = len(data[0])

    while q:
        i, j = q.pop(0)
        
        val = data[i][j]
        candidates = []
        if i > 0 and data[i-1][j] >= val:
            candidates.append((i-1, j))
        if i < l-1 and data[i+1][j] >= val:
            candidates.append((i+1, j))
        if j > 0 and data[i][j-1] >= val:
            candidates.append((i, j-1))
        if j < h-1 and data[i][j+1] >= val:
            candidates.append((i, j+1))
        for c in candidates:
            if c not in visited and data[c[0]][c[1]] != 9:
                visited.add(c)
                q.append(c)
    return len(visited)
      

def get_data(filename='day9.txt'):
    return parse_digits_grid(filename)


if __name__=='__main__':
    data = get_data()
    print(solve(data))
    print(solveb(data))
