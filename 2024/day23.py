from helpers import *
from collections import *
from itertools import *
from math import *
from heapq import heappush, heappop, heappushpop, heapify, heapreplace
from functools import cache


example = r"""
kh-tc
qp-kh
de-cg
ka-co
yn-aq
qp-ub
cg-tb
vc-aq
tb-ka
wh-tc
yn-cg
kh-ub
ta-co
de-co
tc-td
tb-wq
wh-td
ta-ka
td-qp
aq-cg
wq-ub
ub-vc
de-ta
wq-aq
wq-vc
wh-yn
ka-de
kh-ta
co-tc
wh-qp
tb-vc
td-yn
"""


with open('day23.txt', 'r') as f:
    actual = f.read()


def find_n_plus_one_connections_for_clique(mapping, clique):
    clique_set = set(clique)
    candidates = set()
    for n in mapping[clique[0]]:
        if n not in clique_set and all(n in mapping[c1] for c1 in clique_set):
            candidates.add(n) 
    return candidates


def add_to_clique(clique, n):
    s = set(clique)
    s.add(n)
    return tuple(sorted(s))


def find_n_plus_one_interconnections(cliques, mapping):
    next_level = set()
    for c in cliques:
        n_plus_one = find_n_plus_one_connections_for_clique(mapping, c)
        for nn in n_plus_one:
            next_level.add(add_to_clique(c, nn))
    return next_level


def find_largest_set(mapping):
    cliques = set()
    for node in mapping:
        for n in mapping[node]:
            cliques.add(tuple(sorted([node, n])))

    while True:
        next_cliques = find_n_plus_one_interconnections(cliques, mapping)
        if len(next_cliques) == 0:
            break
        cliques = next_cliques

    return ','.join(sorted(list(list(cliques)[0])))


def solve1(inp):
    inp = inp.strip().split('\n')
    mapping = defaultdict(set)
    pairs = set()
    for line in inp:
        l,r = line.split('-')
        mapping[l].add(r)
        mapping[r].add(l)
        pairs.add(tuple(sorted([l, r])))

    triplets = find_n_plus_one_interconnections(pairs, mapping)
    count = 0
    for t1, t2, t3 in triplets:
        if t1[0] == 't' or t2[0] == 't' or t3[0] == 't':
            count += 1

    return count


def solve2(inp):
    inp = inp.strip().split('\n')
    mapping = defaultdict(set)
    for line in inp:
        l,r = line.split('-')
        mapping[l].add(r)
        mapping[r].add(l)

    largest_component = find_largest_set(mapping)
    return largest_component


if __name__=='__main__':
    example_ans = solve1(example)
    print(f'example 1:\n {example_ans}')

    actual_ans = solve1(actual)
    print(f'actual 1:\n {actual_ans}')

    example_ans = solve2(example)
    print(f'example 2:\n {example_ans}')

    actual_ans = solve2(actual)
    print(f'actual 2:\n {actual_ans}')

