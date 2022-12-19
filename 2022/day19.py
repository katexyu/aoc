from helpers import *
from collections import *
from itertools import *
from math import *
from heapq import heappush, heappop, heappushpop, heapify, heapreplace
from functools import cache


example = """
"""

actual = """
Blueprint 1: Each ore robot costs 4 ore. Each clay robot costs 4 ore. Each obsidian robot costs 2 ore and 16 clay. Each geode robot costs 4 ore and 16 obsidian.
Blueprint 2: Each ore robot costs 4 ore. Each clay robot costs 4 ore. Each obsidian robot costs 3 ore and 14 clay. Each geode robot costs 4 ore and 8 obsidian.
Blueprint 3: Each ore robot costs 3 ore. Each clay robot costs 4 ore. Each obsidian robot costs 3 ore and 18 clay. Each geode robot costs 4 ore and 16 obsidian.
Blueprint 4: Each ore robot costs 4 ore. Each clay robot costs 3 ore. Each obsidian robot costs 3 ore and 7 clay. Each geode robot costs 2 ore and 7 obsidian.
Blueprint 5: Each ore robot costs 4 ore. Each clay robot costs 4 ore. Each obsidian robot costs 4 ore and 7 clay. Each geode robot costs 2 ore and 16 obsidian.
Blueprint 6: Each ore robot costs 3 ore. Each clay robot costs 3 ore. Each obsidian robot costs 3 ore and 17 clay. Each geode robot costs 4 ore and 8 obsidian.
Blueprint 7: Each ore robot costs 4 ore. Each clay robot costs 3 ore. Each obsidian robot costs 3 ore and 20 clay. Each geode robot costs 2 ore and 19 obsidian.
Blueprint 8: Each ore robot costs 4 ore. Each clay robot costs 3 ore. Each obsidian robot costs 2 ore and 10 clay. Each geode robot costs 4 ore and 10 obsidian.
Blueprint 9: Each ore robot costs 3 ore. Each clay robot costs 3 ore. Each obsidian robot costs 4 ore and 19 clay. Each geode robot costs 4 ore and 7 obsidian.
Blueprint 10: Each ore robot costs 4 ore. Each clay robot costs 3 ore. Each obsidian robot costs 2 ore and 19 clay. Each geode robot costs 3 ore and 13 obsidian.
Blueprint 11: Each ore robot costs 4 ore. Each clay robot costs 4 ore. Each obsidian robot costs 2 ore and 12 clay. Each geode robot costs 3 ore and 15 obsidian.
Blueprint 12: Each ore robot costs 4 ore. Each clay robot costs 3 ore. Each obsidian robot costs 2 ore and 14 clay. Each geode robot costs 4 ore and 11 obsidian.
Blueprint 13: Each ore robot costs 4 ore. Each clay robot costs 3 ore. Each obsidian robot costs 3 ore and 10 clay. Each geode robot costs 2 ore and 10 obsidian.
Blueprint 14: Each ore robot costs 3 ore. Each clay robot costs 3 ore. Each obsidian robot costs 2 ore and 16 clay. Each geode robot costs 3 ore and 14 obsidian.
Blueprint 15: Each ore robot costs 3 ore. Each clay robot costs 4 ore. Each obsidian robot costs 3 ore and 20 clay. Each geode robot costs 3 ore and 14 obsidian.
Blueprint 16: Each ore robot costs 4 ore. Each clay robot costs 4 ore. Each obsidian robot costs 3 ore and 10 clay. Each geode robot costs 2 ore and 14 obsidian.
Blueprint 17: Each ore robot costs 3 ore. Each clay robot costs 4 ore. Each obsidian robot costs 3 ore and 6 clay. Each geode robot costs 2 ore and 10 obsidian.
Blueprint 18: Each ore robot costs 2 ore. Each clay robot costs 3 ore. Each obsidian robot costs 3 ore and 8 clay. Each geode robot costs 3 ore and 20 obsidian.
Blueprint 19: Each ore robot costs 2 ore. Each clay robot costs 4 ore. Each obsidian robot costs 4 ore and 20 clay. Each geode robot costs 3 ore and 14 obsidian.
Blueprint 20: Each ore robot costs 3 ore. Each clay robot costs 4 ore. Each obsidian robot costs 4 ore and 8 clay. Each geode robot costs 2 ore and 10 obsidian.
Blueprint 21: Each ore robot costs 2 ore. Each clay robot costs 4 ore. Each obsidian robot costs 3 ore and 19 clay. Each geode robot costs 4 ore and 13 obsidian.
Blueprint 22: Each ore robot costs 3 ore. Each clay robot costs 3 ore. Each obsidian robot costs 2 ore and 13 clay. Each geode robot costs 3 ore and 12 obsidian.
Blueprint 23: Each ore robot costs 3 ore. Each clay robot costs 4 ore. Each obsidian robot costs 2 ore and 20 clay. Each geode robot costs 4 ore and 7 obsidian.
Blueprint 24: Each ore robot costs 4 ore. Each clay robot costs 3 ore. Each obsidian robot costs 3 ore and 7 clay. Each geode robot costs 3 ore and 9 obsidian.
Blueprint 25: Each ore robot costs 4 ore. Each clay robot costs 3 ore. Each obsidian robot costs 2 ore and 13 clay. Each geode robot costs 2 ore and 9 obsidian.
Blueprint 26: Each ore robot costs 4 ore. Each clay robot costs 4 ore. Each obsidian robot costs 4 ore and 7 clay. Each geode robot costs 4 ore and 17 obsidian.
Blueprint 27: Each ore robot costs 3 ore. Each clay robot costs 3 ore. Each obsidian robot costs 3 ore and 19 clay. Each geode robot costs 3 ore and 17 obsidian.
Blueprint 28: Each ore robot costs 3 ore. Each clay robot costs 3 ore. Each obsidian robot costs 3 ore and 6 clay. Each geode robot costs 2 ore and 16 obsidian.
Blueprint 29: Each ore robot costs 4 ore. Each clay robot costs 4 ore. Each obsidian robot costs 4 ore and 7 clay. Each geode robot costs 2 ore and 19 obsidian.
Blueprint 30: Each ore robot costs 4 ore. Each clay robot costs 3 ore. Each obsidian robot costs 2 ore and 20 clay. Each geode robot costs 3 ore and 9 obsidian.
"""


from dataclasses import dataclass, replace


@dataclass(frozen=True)
class Blueprint:
    idx: int
    ore: int
    clay: int
    obsidian: tuple 
    geode: tuple


example_blueprints = [
    Blueprint(1, 4, 2, (3,14), (2,7)),
    Blueprint(2, 2, 3, (3,8), (3,12))
]


def parse_input(inp):
    inp = inp.strip().split('\n')
    blueprints = []
    for l in inp:
        tokens = l.split(' ')
        bp = Blueprint(
            int(tokens[1].strip(':')),
            int(tokens[6]),
            int(tokens[12]),
            (int(tokens[18]), int(tokens[21])),
            (int(tokens[27]), int(tokens[30]))
        )
        blueprints.append(bp)
    
    return blueprints


actual_blueprints = parse_input(actual)


def dp(cache, bp, nore, nclay, nobs, ngeode, ore, clay, obs, time_left):
    if time_left == 0:
        return 0
    if time_left == 1:
        return ngeode
    key = (nore, nclay, nobs, ngeode, ore, clay, obs, time_left)
    if key in cache:
        return cache[key]
    best = 0

    max_ore_needed = max(bp.ore, bp.clay, bp.obsidian[0], bp.geode[0])
    max_clay_needed = bp.obsidian[1]
    max_obsidian_needed = bp.geode[1]
    

    # See if you can build anything
    if ore >= bp.ore and time_left > 2 and nore < max_ore_needed:
        n = dp(cache, bp, nore + 1, nclay, nobs, ngeode, ore + nore - bp.ore, clay + nclay, obs + nobs, time_left - 1)
        best = max(n, best)
    if ore >= bp.clay and time_left > 3 and nclay < max_clay_needed:
        n = dp(cache, bp, nore, nclay + 1, nobs, ngeode, ore + nore - bp.clay, clay + nclay, obs + nobs, time_left - 1)
        best = max(n, best)
    if ore >= bp.obsidian[0] and clay >= bp.obsidian[1] and time_left > 2 and nobs < max_obsidian_needed:
        n = dp(cache, bp, nore, nclay, nobs + 1, ngeode, ore + nore - bp.obsidian[0], clay + nclay - bp.obsidian[1], obs + nobs, time_left - 1)
        best = max(n, best)
    if ore >= bp.geode[0] and obs >= bp.geode[1]:
        n = dp(cache, bp, nore, nclay, nobs, ngeode + 1, ore + nore - bp.geode[0], clay + nclay, obs + nobs - bp.geode[1], time_left - 1)
        best = max(n, best)

    # Can also do nothing and just collect resources
    n = dp(cache, bp, nore, nclay, nobs, ngeode, ore + nore, clay + nclay, obs + nobs, time_left - 1)
    best = max(n, best)
    cache[key] = ngeode + best
    return ngeode + best


def calc_quality_level(bp, time=24):
    print(f"Calculating for {bp}, time = {time}")
    cache = dict()
    best = dp(cache, bp, 1, 0, 0, 0, 0, 0, 0, time)
    print(f"Best for {bp.idx} was {best}")
    return bp.idx * best 

   
def best(bp, time=32): 
    print(f"Calculating for {bp}, time = {time}")
    cache = dict()
    best = dp(cache, bp, 1, 0, 0, 0, 0, 0, 0, time)
    print(f"Best for {bp.idx} was {best}")
    return best 


def solvea(inp):
    return sum(calc_quality_level(bp) for bp in inp) 


# This took like 1m30s to run
def solve(inp):
    return prod(best(bp, 32) for bp in inp) 


if __name__=='__main__':
    #example_ans = solvea(example_blueprints)
    #print(f'example:\n {example_ans}')
    #actual_ans = solvea(actual_blueprints)
    #print(f'actual:\n {actual_ans}')


    actual_ans = solve(actual_blueprints[:3])
    print(f'actual:\n {actual_ans}')

