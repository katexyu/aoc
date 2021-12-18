from helpers import *
from collections import *
from itertools import *
from math import *
from heapq import heappush, heappop, heappushpop, heapify, heapreplace
from functools import cache
from json import loads
from copy import deepcopy


example = """
[[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]
[[[5,[2,8]],4],[5,[[9,9],0]]]
[6,[[[6,2],[5,6]],[[7,6],[4,7]]]]
[[[6,[0,7]],[0,9]],[4,[9,[9,0]]]]
[[[7,[6,4]],[3,[1,3]]],[[[5,5],1],9]]
[[6,[[7,3],[3,2]]],[[[3,8],[5,7]],4]]
[[[[5,4],[7,7]],8],[[8,3],8]]
[[9,3],[[9,9],[6,[4,9]]]]
[[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]
[[[[5,2],5],[8,[3,7]]],[[5,[7,5]],[4,4]]]
"""

actual = """
[[0,[[0,9],[6,5]]],[[[5,3],[0,4]],[8,3]]]
[[[[8,6],4],[2,5]],[[[7,4],[4,3]],[[3,4],[3,3]]]]
[[[6,[0,2]],[5,[7,4]]],[1,2]]
[[[[5,4],0],[[5,3],[1,4]]],[[[8,9],[0,0]],1]]
[[[7,0],2],[0,[4,2]]]
[4,[6,2]]
[[[[9,5],[3,4]],[[9,4],[5,3]]],[5,[[0,3],[4,4]]]]
[[[6,0],[3,4]],[9,[[0,3],3]]]
[[[[4,0],5],2],[[4,7],[9,0]]]
[[[2,4],[[3,6],[5,5]]],[[9,[1,1]],[1,1]]]
[[[[8,8],1],8],0]
[[0,6],[[[1,1],8],[[1,7],[6,3]]]]
[[4,8],[[1,[8,4]],[[5,9],[6,3]]]]
[3,[[0,[0,8]],[[2,5],9]]]
[[[[8,8],[5,8]],[[5,2],3]],[[[6,5],2],[6,8]]]
[[[5,[0,8]],[[8,3],[0,4]]],[[[2,5],8],[[0,4],3]]]
[[[7,5],2],[[[3,6],[1,7]],[1,[6,2]]]]
[[[[7,7],1],4],[[8,[5,1]],4]]
[[[[5,0],[9,0]],[[3,3],[1,0]]],[[0,[8,9]],7]]
[[[[4,0],[8,9]],[1,9]],[[[1,7],[9,5]],[[1,4],[9,5]]]]
[[7,0],5]
[[[[3,7],3],[[1,1],[4,9]]],[2,[6,3]]]
[[2,[6,[4,4]]],[0,[0,[6,3]]]]
[[[3,[5,3]],4],[0,4]]
[7,[[[8,8],[6,3]],[9,5]]]
[[7,[4,4]],[5,7]]
[[6,3],[[2,0],[9,6]]]
[[[0,[7,9]],[[5,6],0]],[[4,[8,9]],[8,[3,6]]]]
[[5,[3,[7,0]]],[[4,1],[[1,1],[3,0]]]]
[[9,[2,4]],[[2,[8,1]],[[4,5],1]]]
[[8,[0,[8,2]]],[[2,4],[[2,6],8]]]
[[[[8,1],5],2],[0,[[5,7],8]]]
[[[[9,2],[6,0]],[3,[9,6]]],[[[2,1],0],[[6,2],[2,0]]]]
[[[[6,6],1],[2,3]],[9,[[4,8],5]]]
[[3,[[1,5],[8,4]]],[[6,6],3]]
[[[4,8],5],3]
[[0,[[5,4],[9,7]]],[[[0,5],[7,6]],[[6,9],[1,9]]]]
[[[9,[1,1]],[7,[2,9]]],[[6,[3,6]],[[4,5],[1,0]]]]
[[[5,[7,7]],9],2]
[1,[[0,[3,2]],[1,[8,7]]]]
[5,[[5,[3,5]],[[4,1],[8,3]]]]
[[0,4],[[[2,6],7],3]]
[5,9]
[[[[9,2],[3,9]],3],[0,[[8,4],0]]]
[[[9,7],[6,[3,3]]],3]
[2,[[4,0],[8,[8,4]]]]
[[2,4],[9,[[2,9],4]]]
[[[[9,7],[9,5]],[[9,2],[3,9]]],0]
[2,[0,[[2,2],6]]]
[[[[8,9],[7,9]],[3,[1,4]]],[[1,[9,5]],[[1,9],7]]]
[[[1,[3,6]],0],[9,[8,[2,2]]]]
[[[7,3],[[7,2],[4,3]]],[[9,[7,7]],7]]
[[[3,[6,4]],4],[[[8,9],[6,6]],[1,[9,1]]]]
[[[[6,3],[1,8]],[6,9]],[[[0,0],2],0]]
[[[8,9],7],1]
[[[[3,2],[7,5]],2],9]
[[[[4,9],5],4],[0,[[2,4],[7,8]]]]
[[[[8,1],[6,5]],[[8,1],[9,7]]],9]
[0,[1,6]]
[[[5,9],[[9,8],6]],[0,[5,[1,2]]]]
[9,[[[4,3],5],[9,3]]]
[[[9,[2,7]],[2,[9,0]]],[[1,[8,7]],[[3,5],[2,6]]]]
[9,[[3,8],[[4,5],[7,1]]]]
[[0,[2,8]],[[6,3],5]]
[[[6,[2,5]],[[2,1],8]],[5,[[4,9],[0,3]]]]
[[[[0,4],3],[[1,3],[3,2]]],9]
[9,[[2,8],[[3,8],7]]]
[[[4,[1,9]],[3,3]],[0,[[4,3],[1,7]]]]
[[6,[[5,2],[2,5]]],[1,[[0,0],[1,4]]]]
[9,[1,[7,[5,6]]]]
[[5,4],6]
[6,[[5,6],7]]
[[[3,[6,0]],[8,[3,5]]],[[5,1],[[7,9],3]]]
[[[6,[8,7]],[[5,2],0]],[[6,[4,0]],[1,[1,2]]]]
[3,[[[7,8],0],[[6,5],0]]]
[[4,9],[9,9]]
[[7,[5,[9,7]]],1]
[[[3,[3,3]],[4,6]],[[[9,5],[4,8]],[5,[2,0]]]]
[[[[8,6],6],8],[3,1]]
[6,[5,0]]
[2,[[2,[7,5]],[6,[0,6]]]]
[[[9,[1,3]],[0,[9,4]]],4]
[[[[2,5],[9,9]],[[8,2],2]],[9,[1,[9,1]]]]
[[[[8,9],0],[[2,5],[2,2]]],[[7,[4,1]],[[3,9],[5,8]]]]
[[[7,6],[6,3]],5]
[2,[[[5,8],[1,2]],0]]
[[[8,7],[6,4]],[[[0,6],2],[[2,1],5]]]
[2,1]
[0,[[[4,3],[6,6]],8]]
[4,2]
[[[6,[3,2]],[5,[2,3]]],[[[3,5],[6,2]],[1,[6,6]]]]
[[0,[[8,1],[0,5]]],[[[3,3],3],[[6,8],5]]]
[[[3,0],[4,[6,5]]],[[[3,3],[4,0]],6]]
[[[[7,3],4],4],[[7,[8,2]],0]]
[[[4,3],[0,9]],[[1,[8,9]],[[3,0],0]]]
[[3,2],[2,[[2,6],[2,1]]]]
[2,8]
[[[[1,4],[7,3]],[8,[2,1]]],4]
[[[1,7],[1,[4,8]]],[[[2,2],[6,1]],[[9,9],8]]]
[[[5,[7,2]],[[8,6],6]],[1,5]]
"""


def solve(inp):
    inp = inp.strip().split('\n')
    inp = list(map(loads, inp))
    
    s = sum_all(inp)
    ans = magnitude(s)
    return ans


def solveb(inp):
    inp = inp.strip().split('\n')
    inp = list(map(loads, inp))
    
    best = 0
    for i in range(len(inp)):
        for j in range(len(inp)):
            if i == j:
                continue
            result = magnitude(sum_all([inp[i], inp[j]]))
            best = max(best, result)
    return best


def sum_all(lines):
    cur = lines[0]
    for i in range(1, len(lines)):
       l = lines[i]
       cur = do_reduce([cur, l])

    return cur
 

def do_reduce(line):
    res = deepcopy(line)
    while True:
        res, _, exploded = explode(res, 0)
        if not exploded:
            prev = res
            res, is_split = split(res)
            if not is_split:
                break 
    return res
        

def explode(line, depth):
    left = line[0]
    right = line[1]

    if isinstance(left, int) and isinstance(right, int):
        if depth >= 4:
            # explode
            return 0, (left, right), True
        return [left, right], (0, 0), False
    if isinstance(left, list) and isinstance(right, list):
        left, el, exploded_left = explode(left, depth+1)
        if exploded_left:
            add_to_first(right, el[1])
            return [left, right], (el[0], 0), exploded_left

        right, er, exploded_right = explode(right, depth+1)
        add_to_last(left, er[0])
        return [left, right], (0, er[1]), exploded_right
    elif isinstance(left, list):
        l, e, exploded = explode(left, depth+1)
        if exploded:
            return [l, right + e[1]], (e[0], 0), True
        return [l, right], (0, 0), False
    elif isinstance(right, list):
        r, e, exploded = explode(right, depth+1)
        if exploded:
            return [left + e[0], r], (0, e[1]), True
        return [left, r], (0, 0), False
    

def add_to_first(a, val):
    cur = a
    while isinstance(cur, list):
        if isinstance(cur[0], int):
            cur[0] += val
            return
        cur = cur[0] 


def add_to_last(a, val):      
    cur = a
    while isinstance(cur, list):
        if isinstance(cur[-1], int):
            cur[-1] += val 
            return
        cur = cur[-1] 


def split(num):
    if isinstance(num, int):
        if num < 10:
            return num, False
        left = num // 2
        right = num - left
        return [left, right], True
    left, right = num
    sleft, is_split = split(left)
    if is_split:
        return [sleft, right], is_split
    sright, is_split = split(right)
    return [left, sright], is_split


def magnitude(num):
    if isinstance(num, int):
        return num

    left, right = num
    return 3 * magnitude(left) + 2 * magnitude(right)


if __name__=='__main__':
    example_ans = solveb(example)
    print(f'example:\n {example_ans}')

    actual_ans = solveb(actual)
    print(f'actual:\n {actual_ans}')

