from helpers import *
from collections import *
from itertools import *
from math import *
from heapq import heappush, heappop, heappushpop, heapify, heapreplace
from functools import cache


example = r"""
jqt: rhn xhk nvd
rsh: frs pzl lsr
xhk: hfx
cmg: qnr nvd lhk bvb
rhn: xhk bvb hfx
bvb: xhk hfx
pzl: lsr hfx nvd
qnr: nvd
ntq: jqt hfx bvb xhk
nvd: lhk
lsr: lhk
rzs: qnr cmg lsr rsh
frs: qnr lhk lsr
"""

with open('day25.txt', 'r') as f:
    actual = f.read()


from copy import deepcopy
import random


def solve1(inp):
    inp = inp.strip().split('\n')
    d = defaultdict(list)
    for line in inp:
        l,r = line.split(': ')
        rr = r.split()
        for r in rr:
            d[l].append(r)
            d[r].append(l)

    for i in range(100):
        dd = deepcopy(d)
        res = kargerish(dd)
        if res is not None:
            g = [v for v in res.values()]
            return len(g[0]) * len(g[1])


def kargerish(d):
    groups = defaultdict(set)
    while len(d) > 2:
        # Select a random edge to contract
        v1 = random.choice([k for k in d])
        v2 = random.choice(d[v1])

        # Keep track of which original nodes belong to what group
        v1 = reassign_to_group(v1, d, groups)
        v2 = reassign_to_group(v2, d, groups)
        contract(d, v1, v2, groups)
    mincut = len(d[[k for k in d][0]])
    if mincut == 3:
        return groups


def reassign_to_group(v, d, groups):
    if v in groups:
        return v
    g = 0
    if len(groups) > 0:
        g = max(groups.keys()) +1
    groups[g].add(v)
    d[g] = d[v][:]
    for n in d[v]:
        d[n].remove(v)
        d[n].append(g)
    del d[v]
    return g


def contract(d, v1, v2, groups):
    # assign all of v2's edges to v1
    for n in d[v2]:
        if n != v1:
            d[v1].append(n)
        d[n].remove(v2)
        if n != v1:
            d[n].append(v1)
        groups[v1].update(groups[v2])
        del groups[v2]
    del d[v2]
    return v1, v2


if __name__=='__main__':
    example_ans = solve1(example)
    print(f'example 1:\n {example_ans}')
    assert example_ans == 54

    actual_ans = solve1(actual)
    print(f'actual 1:\n {actual_ans}')

