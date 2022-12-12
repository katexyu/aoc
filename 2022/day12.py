from helpers import *
from collections import *
from itertools import *
from math import *
from heapq import heappush, heappop, heappushpop, heapify, heapreplace
from functools import cache


example = """
Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi
"""

actual = """
abcccccaaaccccaacaaccaaaaaaaaaaaaaaaaaaaaccccccccccccccccccccccccccccccccccaaaaaa
abcccccaaaacccaaaaaccaaaaaaaaaaaaaaaaaaaaacccccccccccccccccccccccccccccccccccaaaa
abcccccaaaaccaaaaaccccaaaccaaaaaacccacaaaaccccccccccccccccaaaccccccccccccccccaaaa
abcccccaaacccaaaaaaccccccccaaaaaacccccaaccccccccccccccccccaaaccccccccccccccccaaaa
abcccccccccccccaaaacccccccaaaaaaaaccccccccccccccccccccccccaaacccccccccccccccaaaaa
abccccccaacccccaacccccccccaaaaaaaaccccccccccccccccccccccccaaaaccaaacccccccccccccc
abccccccaacccccccccccccccaaacccaaaacccaacaaccccccccccacaccaaacaajaacccccccccccccc
abcccaaaaaaaaccccacccccccaaaccccaaacccaaaaaccccccccccaaaaaaajjjjkkkccccccaacccccc
abcccaaaaaaaacaaaacccccccccccccccccccaaaaaccccccccciiiijjjjjjjjjkkkkcaaaaaacccccc
abcccccaaaacccaaaaaacccccccccccccccccaaaaaacccccciiiiiijjjjjjjrrrkkkkaaaaaaaacccc
abcccccaaaaacccaaaacccccccccaacccccccccaaaaccccciiiiiiiijjjjrrrrrsskkaaaaaaaacccc
abccccaaaaaaccaaaaacccccccccaaaacccccccaccccccciiiiqqqqrrrrrrrrrssskkkaaaaaaacccc
abaaccaaccaaccaacaacccccccaaaaaaccccccccccccccciiiqqqqqrrrrrrruussskkkaaaaacccccc
abaaaacccccccccccccccccccccaaaaccccccccaaaccccciiqqqqqttrrrruuuuussskkaaaaacccccc
abaaaacccccccccccccccccccccaaaaaccccccccaaaaccchiqqqtttttuuuuuuuussskkcccaacccccc
abaaacccccaaaccacccccccccccaacaaccccccaaaaaaccchhqqqtttttuuuuxxuussslllcccccccccc
abaaaaccccaaaaaacaaccccccaccccccccccccaaaaacccchhqqqttxxxxuuxxyyusssllllccccccccc
abacaaccccaaaaaacaaaaaaaaaaccccccccccccaaaaaccchhqqqttxxxxxxxxyuusssslllccccccccc
abcccccccaaaaaaacaaaaaaaaaccccaacccccccaaccaccchhhqqtttxxxxxxyyvvvsssslllcccccccc
abcccccccaaaaaaaaaaaaaaaaaccccaaaaccccccccccccchhhppqttxxxxxyyyvvvvsqqqlllccccccc
SbcccaaccaaaaaaaaaaaaaaaaaacaaaaaacccccccccccchhhhpptttxxxEzzyyyyvvvqqqqlllcccccc
abcccaaccccaaacaaaaaaaaaaaaacaaaaccccccccccccchhhppptttxxxyyyyyyyyvvvqqqlllcccccc
abaaaaaaaacaaacaaaaaaaaaaaaacaaaaacaaccccccccchhpppsssxxyyyyyyyyvvvvvqqqlllcccccc
abaaaaaaaaccccccccaaacaaaccccaacaaaaaccccccaagggpppsswwwwwwyyyvvvvvvqqqmmmmcccccc
abccaaaaccccaacaacaaacaaacccccccccaaacaaaccaagggppssswwwwwwyyywvvqqqqqqmmmccccccc
abcaaaaaccccaaaaacaaccaaccaaaccaaaaaaaaaaaaaagggppsssswwwswwyywvrqqqqmmmmcccccccc
abcaaaaaaccaaaaacccccccccaaaaccaaaaaaaaaacaaagggpppssssssswwwwwwrrqmmmmmccccccccc
abcaacaaaccaaaaaaccccccccaaaaccccaaaaaacccaaagggppppssssssrwwwwrrrmmmmmdccccccccc
abccccaaaccaaaaaaccccccccaaaaccccaaaaaacccaacggggpooooooosrrwwwrrnmmmddddcacccccc
abccccaaaaaaaacccccccccccccccccccaaaaaaaccccccggggoooooooorrrrrrrnnmdddddaaaacccc
abcccccaaaaaaccccccccccccccccccccaaacaaacccccccggggfffooooorrrrrrnnddddaaaaaacccc
abccaaaaaaaacccccccccccccccccccccaccccccccccccccggffffffooonrrrrnnndddaaaaaaacccc
abccaaaaaaaaaccccaacccccccccccccccccccccccccccccccfffffffoonnnnnnndddcaaaaacccccc
abccaaaaaaaaaacccaaccccccccccccccaccccccccccccccccccccffffnnnnnnnedddaaaaaacccccc
abcccccaaaaaaaaaaaacccccccaccccaaacccccccccccccccccccccfffeennnneeedcccccaacccccc
abcccccaaacccaaaaaaaaccccaaacccaaaccacccccccccccccccccccafeeeeeeeeecccccccccccccc
abcccccaaccccaaaaaaaaacccaaaaaaaaaaaaccccccaaaccccccccccaaeeeeeeeeeccccccccccccca
abaccccccccccaaaaaaaaacccaaaaaaaaaaacccccccaaaaacccccccaaaaceeeeecccccccccccaccca
abaccccccccccaaaaaaaaccaaaaaaaaaaaaaacccccaaaaaccccccccaaaccccaaacccccccccccaaaaa
abaccccccccccaaaaaaacccaaaaaaaaaaaaaacccccaaaaacccccccccccccccccccccccccccccaaaaa
abaccccccccccaccaaaacccaaaaaaaaaaaaaaccccccaaaaaccccccccccccccccccccccccccccaaaaa
"""


def solvea(inp, start):
    inp = inp.strip('\n').split()
    grid = list(map(list, inp))
    
    return min_steps(grid, start) 


def min_steps(grid, start):
    visited = {
        start: 0
    }
    distance = 0
    q = deque([(start[0], start[1], 0)])
    while q:
        x, y, dist = q.popleft()
        prev = grid[x][y]
        for i, j in each_neighbors(grid, x, y):
            val = grid[i][j]
            if height(prev) >= height(val)-1 and val == 'E':
                return dist + 1
            if height(val) > height(prev) + 1:
                continue
            elif (i, j) not in visited and val != 'E':
                q.append((i, j, dist+1))
                visited[(i, j)] = dist+1
    return 1000000000


def height(val):
    if val == 'E':
        return ord('z')
    if val == 'S':
        return ord('a')
    return ord(val)


def solveb(inp, start):
    inp = inp.strip().split('\n')
    grid = list(map(list, inp))

    start_points = [start]
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            val = grid[i][j]
            if val == 'a':
                start_points.append((i, j))

    return min(min_steps(grid, start_point) for start_point in start_points)


def each_neighbors(grid, x, y):
    deltas = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    for dx, dy in deltas:
        if 0 <= x+dx <len(grid) and 0 <= y+dy < len(grid[0]):
            yield (x+dx, y+dy)


if __name__=='__main__':
    example_ans = solvea(example, (0,0))
    print(f'example:\n {example_ans}')

    actual_ans = solvea(actual, (20,0))
    print(f'actual:\n {actual_ans}')

    example_ans = solveb(example, (0,0))
    print(f'example:\n {example_ans}')

    actual_ans = solveb(actual, (20,0))
    print(f'actual:\n {actual_ans}')

