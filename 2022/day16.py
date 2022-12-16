from helpers import *
from collections import *
from itertools import *
from math import *
from heapq import heappush, heappop, heappushpop, heapify, heapreplace
from functools import cache


example = """
Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
Valve BB has flow rate=13; tunnels lead to valves CC, AA
Valve CC has flow rate=2; tunnels lead to valves DD, BB
Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE
Valve EE has flow rate=3; tunnels lead to valves FF, DD
Valve FF has flow rate=0; tunnels lead to valves EE, GG
Valve GG has flow rate=0; tunnels lead to valves FF, HH
Valve HH has flow rate=22; tunnel leads to valve GG
Valve II has flow rate=0; tunnels lead to valves AA, JJ
Valve JJ has flow rate=21; tunnel leads to valve II
"""

actual = """
Valve FY has flow rate=0; tunnels lead to valves TG, CD
Valve EK has flow rate=12; tunnels lead to valves JE, VE, PJ, CS, IX
Valve NU has flow rate=0; tunnels lead to valves FG, HJ
Valve AY has flow rate=0; tunnels lead to valves EG, KR
Valve DH has flow rate=0; tunnels lead to valves FX, VW
Valve IX has flow rate=0; tunnels lead to valves VW, EK
Valve DZ has flow rate=0; tunnels lead to valves HT, FG
Valve YE has flow rate=0; tunnels lead to valves CI, MS
Valve OO has flow rate=0; tunnels lead to valves FX, CS
Valve SB has flow rate=0; tunnels lead to valves RR, AP
Valve HT has flow rate=4; tunnels lead to valves DZ, GA, CI, DE, JS
Valve MS has flow rate=11; tunnels lead to valves PJ, WG, CA, YE
Valve CD has flow rate=0; tunnels lead to valves UW, FY
Valve IZ has flow rate=0; tunnels lead to valves XF, AP
Valve JE has flow rate=0; tunnels lead to valves EK, TQ
Valve DN has flow rate=0; tunnels lead to valves KR, VE
Valve VW has flow rate=13; tunnels lead to valves DH, IX
Valve UH has flow rate=0; tunnels lead to valves MN, TQ
Valve TB has flow rate=0; tunnels lead to valves AP, BJ
Valve XT has flow rate=0; tunnels lead to valves TQ, UW
Valve RR has flow rate=0; tunnels lead to valves FG, SB
Valve BJ has flow rate=0; tunnels lead to valves TB, AA
Valve DE has flow rate=0; tunnels lead to valves HT, WI
Valve MT has flow rate=0; tunnels lead to valves EW, FG
Valve HJ has flow rate=0; tunnels lead to valves KS, NU
Valve WI has flow rate=3; tunnels lead to valves XF, DX, DE, EW
Valve KI has flow rate=0; tunnels lead to valves GW, TQ
Valve JS has flow rate=0; tunnels lead to valves UW, HT
Valve XF has flow rate=0; tunnels lead to valves WI, IZ
Valve VE has flow rate=0; tunnels lead to valves DN, EK
Valve CI has flow rate=0; tunnels lead to valves YE, HT
Valve GW has flow rate=0; tunnels lead to valves EG, KI
Valve TQ has flow rate=14; tunnels lead to valves WG, KI, JE, UH, XT
Valve AA has flow rate=0; tunnels lead to valves BJ, CF, DX, RB, AQ
Valve EW has flow rate=0; tunnels lead to valves MT, WI
Valve UW has flow rate=6; tunnels lead to valves XT, CD, NZ, JS
Valve MN has flow rate=0; tunnels lead to valves KR, UH
Valve FG has flow rate=8; tunnels lead to valves NU, RR, MT, MK, DZ
Valve RB has flow rate=0; tunnels lead to valves NZ, AA
Valve AQ has flow rate=0; tunnels lead to valves AA, MK
Valve WG has flow rate=0; tunnels lead to valves TQ, MS
Valve YW has flow rate=0; tunnels lead to valves CA, KR
Valve CA has flow rate=0; tunnels lead to valves YW, MS
Valve PJ has flow rate=0; tunnels lead to valves MS, EK
Valve EG has flow rate=23; tunnels lead to valves AY, GW
Valve NC has flow rate=0; tunnels lead to valves TG, KS
Valve WY has flow rate=16; tunnel leads to valve VQ
Valve AP has flow rate=7; tunnels lead to valves IZ, VQ, TB, SB
Valve CF has flow rate=0; tunnels lead to valves GA, AA
Valve FX has flow rate=20; tunnels lead to valves DH, OO
Valve NZ has flow rate=0; tunnels lead to valves RB, UW
Valve KS has flow rate=19; tunnels lead to valves NC, HJ
Valve VQ has flow rate=0; tunnels lead to valves WY, AP
Valve TG has flow rate=17; tunnels lead to valves NC, FY
Valve GA has flow rate=0; tunnels lead to valves CF, HT
Valve CS has flow rate=0; tunnels lead to valves OO, EK
Valve MK has flow rate=0; tunnels lead to valves AQ, FG
Valve KR has flow rate=18; tunnels lead to valves MN, DN, YW, AY
Valve DX has flow rate=0; tunnels lead to valves AA, WI
"""


def parse_line(l):
    tokens = l.split(' ')
    valve = tokens[1]
    flow_rate = int(tokens[4].split('=')[1].strip(';'))
    valves = [v.strip(',') for v in tokens[9:]]
    return valve, flow_rate, valves


cache = {}


def solvea(inp):
    inp = inp.strip().split('\n')
   
    neighbors = {} 
    flow_rates = {}
    current = 'AA'
    cache.clear()
    for line in inp:
        valve, flow_rate, valves = parse_line(line)
        neighbors[valve] = valves
        flow_rates[valve] = flow_rate

    ans = do_stepa(0, current, flow_rates, neighbors, []) 
    return ans


# This takes like 2 min to run, but w/e it works
def solveb(inp):
    inp = inp.strip().split('\n')
   
    neighbors = {} 
    flow_rates = {}
    currenta, currentb = 'AA', 'AA'
    cache.clear()
    for line in inp:
        valve, flow_rate, valves = parse_line(line)
        neighbors[valve] = valves
        flow_rates[valve] = flow_rate

    ans = do_step(0, currenta, currentb, flow_rates, neighbors, []) 
    return ans


def do_step(minute, currenta, currentb, flow_rates, neighbors, open_valves):
    # It doesn't matter who does what, so just pick a consistent a and b here to halve the solution space
    a = min(currenta, currentb)
    b = max(currenta, currentb)
    open_valves.sort()
    if (minute, a, b, tuple(open_valves)) in cache:
        return cache[(minute, a, b, tuple(open_valves))]
    if minute == 26:
        return 0
    flow = sum(flow_rates[o] for o in open_valves)
    opened = -1
    neighbor = -1

    # Options are: open valveA, open valveB, A visit neighbor, B visit neighbor
    flow_ratea = flow_rates[a]
    flow_rateb = flow_rates[b]
    # Open Valve A
    if a not in open_valves and flow_ratea > 0:
        new_open_valves = open_valves + [a]

        # See if you can open Valve B
        if b != a and b not in open_valves and flow_rateb > 0:
            new_open_valves.append(b)
            opened = do_step(minute + 1, a, b, flow_rates, neighbors, new_open_valves)

        else:
            # see which valve B should move to
            for n in neighbors[b]:
                visit_neighbor = do_step(minute + 1, a, n, flow_rates, neighbors, new_open_valves)
                neighbor = max(neighbor, visit_neighbor)

    elif b not in open_valves and flow_rateb > 0:
        new_open_valves = open_valves + [b]

        # see which valve A should move to
        for n in neighbors[a]:
            visit_neighbor = do_step(minute + 1, n, b, flow_rates, neighbors, new_open_valves)
            neighbor = max(neighbor, visit_neighbor)

    else: # They both visit a neighbor
        for an in neighbors[a]:
            for bn in neighbors[b]:
                visit_neighbor = do_step(minute + 1, an, bn, flow_rates, neighbors, open_valves)
                neighbor = max(neighbor, visit_neighbor)

    best = max(opened, neighbor)
    
    cache[(minute, a, b, tuple(open_valves))] = flow + best
    return flow + best 



def do_stepa(minute, current, flow_rates, neighbors, open_valves):
    open_valves.sort()
    if (minute, current, tuple(open_valves)) in cache:
        return cache[(minute, current, tuple(open_valves))]
    if minute == 30:
        return 0
    # either open the valve or move to a neighbor
    flow = sum(flow_rates[o] for o in open_valves)
    opened = -1
    neighbor = -1

    flow_rate = flow_rates[current]
    if current not in open_valves and flow_rate > 0:
        new_open_valves = open_valves + [current]
        opened = do_stepa(minute + 1, current, flow_rates, neighbors, new_open_valves)

    # Move to a neighbor
    for n in neighbors[current]:
        visit_neighbor = do_stepa(minute + 1, n, flow_rates, neighbors, open_valves)
        neighbor = max(neighbor, visit_neighbor)

    best = max(opened, neighbor)
    
    cache[(minute, current, tuple(open_valves))] = flow + best
    return flow + best 


if __name__=='__main__':
    example_ans = solvea(example)
    print(f'example:\n {example_ans}')

    actual_ans = solvea(actual)
    print(f'actual:\n {actual_ans}')

    example_ans = solveb(example)
    print(f'example:\n {example_ans}')

    actual_ans = solveb(actual)
    print(f'actual:\n {actual_ans}')

