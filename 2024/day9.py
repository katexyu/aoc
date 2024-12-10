from helpers import *
from collections import *
from itertools import *
from math import *
from heapq import heappush, heappop, heappushpop, heapify, heapreplace
from functools import cache


example = r"""
2333133121414131402
"""


with open('day9.txt', 'r') as f:
    actual = f.read()


def solve2(inp):
    inp = inp.strip().split('\n')[0]
    inp += '0'
    
    blocks = []

    total_blocks = 0
    total_length = 0
    ids = defaultdict(list)

    for i in range(len(inp)//2):
        num_blocks = int(inp[i*2])
        total_blocks += num_blocks
        free = int(inp[i*2+1])
        ids[i] = [num_blocks, num_blocks, free, total_length]
        total_length += num_blocks + free
        blocks.extend([i]*num_blocks)
        blocks.extend([-1]*free)

    # last block is just last
    last = total_length - 1

    current_free = 0
    cur = i
    while cur > 0:
        # Check if file could be moved earlier
        num_blocks, _, _, cl = ids[cur]

        for j in range(cur):
            starting, tot, free, l = ids[j]
            if num_blocks <= free:
                for x in range(num_blocks):
                    blocks[x + l + tot] = cur
                ids[j][1] += num_blocks
                ids[j][2] -= num_blocks
                for x in range(cl, cl+num_blocks):
                    blocks[x] = -1
                break
        cur -= 1

    ans = compute_checksum(blocks, len(blocks))
    return ans


def compute_checksum(arr, end):
    s = 0
    for i in range(end):
        if arr[i] == -1:
            continue
        s += i * arr[i]
    return s


def solve1(inp):
    inp = inp.strip().split('\n')[0]
    inp += '0'

    blocks = []

    total_blocks = 0
    total_length = 0
    ids = defaultdict(list)

    for i in range(len(inp)//2):
        num_blocks = int(inp[i*2])
        total_blocks += num_blocks
        free = int(inp[i*2+1])
        ids[i] = (num_blocks, free, total_length, total_length + num_blocks + free)
        total_length += num_blocks + free
        blocks.extend([i]*num_blocks)
        blocks.extend([-1]*free)

    last = total_length - 1

    first_id_free = 0
    first_idx = 0

    while True:
        num_blocks, free, l, h = ids[first_id_free]
        if free > 0:
            first_idx = num_blocks + l
            break
        first_id_free += 1
    
    current_free = 0
    while last > total_blocks-1:
        if blocks[last] == -1:
            last -= 1
            continue
        i = blocks[last]
        if blocks[first_idx] != -1:
            raise "something went wrong, found non free id"
        blocks[first_idx] = i
        blocks[last] = -1
        num_blocks, free, l, h = ids[first_id_free]
        first_idx += 1
        if first_idx == h:
            first_id_free += 1
            # go to the next one 
            while True:
                num_blocks, free, l, h = ids[first_id_free]
                if free > 0:
                    first_idx = num_blocks + l
                    break
                first_id_free += 1
        last -= 1
    
    ans = compute_checksum(blocks, total_blocks)
    return ans


if __name__=='__main__':
    example_ans = solve1(example)
    print(f'example 1:\n {example_ans}')

    actual_ans = solve1(actual)
    print(f'actual 1:\n {actual_ans}')

    example_ans = solve2(example)
    print(f'example 2:\n {example_ans}')

    actual_ans = solve2(actual)
    print(f'actual 2:\n {actual_ans}')

