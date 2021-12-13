from helpers import *
from collections import defaultdict


def solve(data):
    paths = set()
    q = [(['start'], 'start')]
    while q:
        (path, node) = q.pop(0)
        neighbors = data[node]
        for n in neighbors:
            if n == 'start':
                continue
            new_path = path + [n]
            if n == 'end':
                paths.add(','.join(new_path))
                continue

            if n.isupper() or can_add(path, n):
                q.append((new_path, n))
    return len(paths), paths
        

def print_path(path):
    return ','.join(path)


def can_add(path, elem):
    return elem not in path


def can_add_b(l, elem):
    counts = defaultdict(int)
    for i in l:
        counts[i] += 1
    elem_count = counts[elem]
    
    for k, v in counts.items():
        if not k.isupper() and k != 'start':
            if v >= 2 and elem_count > 0:
                return False
    return True


def get_data(filename='day12.txt'):
    mapping = defaultdict(set)
    for l in parse_lines(filename):
        parts = l.split('-')
        mapping[parts[0]].add(parts[1])
        mapping[parts[1]].add(parts[0])
    return mapping


if __name__=='__main__':
    data = get_data()
    ans, out = solve(data)
    print(ans)


