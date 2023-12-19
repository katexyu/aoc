from helpers import *
from collections import *
from itertools import *
from math import *
from heapq import heappush, heappop, heappushpop, heapify, heapreplace
from functools import cache


example = r"""
px{a<2006:qkq,m>2090:A,rfg}
pv{a>1716:R,A}
lnx{m>1548:A,A}
rfg{s<537:gd,x>2440:R,A}
qs{s>3448:A,lnx}
qkq{x<1416:A,crn}
crn{x>2662:A,R}
in{s<1351:px,qqz}
qqz{s>2770:qs,m<1801:hdj,R}
gd{a>3333:R,R}
hdj{m>838:A,pv}

{x=787,m=2655,a=1222,s=2876}
{x=1679,m=44,a=2067,s=496}
{x=2036,m=264,a=79,s=2244}
{x=2461,m=1339,a=466,s=291}
{x=2127,m=1623,a=2188,s=1013}
"""

with open('day19.txt', 'r') as f:
    actual = f.read()


from dataclasses import dataclass


@dataclass
class Rule:
    v: str
    gt: bool
    threshold: int
    acc: str
    passthru: bool = False

    def nxt(self, ratings):
        if self.passthru:
            return self.v
        r = ratings[self.v]
        if self.gt:
            return self.acc if r > self.threshold else None
        return self.acc if r < self.threshold else None
    

def solve1(inp):
    w, r = inp.strip().split('\n\n')
    raw_workflows = w.split('\n')
    raw_ratings = r.split('\n')
    workflows = {}
    for w in raw_workflows:
        name, rest = w.strip('}').split('{')
        rules = rest.split(',')
        rules = [parse_rule(r) for r in rules]
        workflows[name] = rules

    ratings = []
    for r in raw_ratings:
        row = {}
        for v in r.strip('{').strip('}').split(','):
            l, r = v.split('=')
            row[l] = int(r)
        ratings.append(row)
    
    ans = 0
    for p in ratings:
        cur = 'in'
        while cur not in ('A','R'):
            w = workflows[cur]
            for r in w:
                cur = r.nxt(p)
                if cur is not None:
                    break
           
        if cur == 'A':
           ans += sum(p.values())
    return ans 


def parse_rule(rule):
    if ':' not in rule:
        return Rule(rule, False, 0, rule, True)
    l, acc = rule.split(':')
    gt = False
    if '>' in l:
        gt = True
        v, val = l.split('>')
    elif '<' in l:
        v, val = l.split('<')
    return Rule(v, gt, int(val), acc)

    
from copy import deepcopy


def solve2(inp):
    w, r = inp.strip().split('\n\n')
    raw_workflows = w.split('\n')
    raw_ratings = r.split('\n')
    workflows = {}
    for w in raw_workflows:
        name, rest = w.strip('}').split('{')
        rules = rest.split(',')
        rules = [parse_rule(r) for r in rules]
        workflows[name] = rules

    reverse_mapping = defaultdict(list)
        
    for w, rules in workflows.items():
        # Figure out what constraints must be true to have reached each node
        base = {'x': [1, 4000], 'm': [1, 4000], 'a': [1, 4000], 's': [1, 4000]}
        for r in rules:
            dst = r.acc
            threshold = r.threshold
            complement = deepcopy(base)
            if r.passthru:
                reverse_mapping[r.v].append((w, base))
                break
            lo, hi = base[r.v]
            if r.gt:
                if threshold < hi:
                    base[r.v][0] = max(lo, threshold+1)
                    # this is the reverse
                    complement[r.v][1] = min(hi, threshold)
                else:
                    complement = base
                    base = None
            else:
                if threshold > lo:
                    base[r.v][1] = min(hi, threshold-1)
                    complement[r.v][0] = max(lo, threshold)
                else:
                    complement = base
                    base = None

            if base is not None:
                reverse_mapping[dst].append((w, base))
            base = complement

    # Work backwards from A until you get to in
    return num_paths(reverse_mapping)



def num_paths(mapping):
    queue = [('A', {'x': [1, 4000], 'm': [1, 4000], 'a': [1, 4000], 's': [1, 4000]})]
    successful_ranges = []
    while queue:
        val, ranges = queue.pop()
        nxt = mapping[val]
        for v, r in nxt:
            overlap = can_use(ranges, r)
            if overlap is not None:
                if v == 'in':
                    successful_ranges.append(overlap)
                else:
                    queue.append((v, overlap))

    total = 0
    for s in successful_ranges:
        ranges = s.values()
        num_vals = 1
        for r in ranges:
            num_vals *= (r[1]-r[0]+1)
        total += num_vals
    return total


def can_use(ranges, rule_ranges):
    overlapping = {}
    for k in ranges:
        r1, r2 = ranges[k], rule_ranges[k]
        overlap = range_overlapping(r1, r2)
        if overlap is None:
            return None
        overlapping[k] = [overlap.start, overlap.stop] 
    return overlapping


def range_overlapping(r, r2):
    return range(max(r[0], r2[0]), min(r[1], r2[1])) or None


if __name__=='__main__':
    example_ans = solve1(example)
    print(f'example 1:\n {example_ans}')
    assert example_ans == 19114

    actual_ans = solve1(actual)
    print(f'actual 1:\n {actual_ans}')

    example_ans = solve2(example)
    print(f'example 2:\n {example_ans}')
    assert example_ans == 167409079868000

    actual_ans = solve2(txtfile)
    print(f'actual 2:\n {actual_ans}')

