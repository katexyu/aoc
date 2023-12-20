from helpers import *
from collections import *
from itertools import *
from math import *
from heapq import heappush, heappop, heappushpop, heapify, heapreplace
from functools import cache


example = r"""
broadcaster -> a, b, c
%a -> b
%b -> c
%c -> inv
&inv -> a
"""

with open('day20.txt', 'r') as f:
    actual = f.read()


from dataclasses import dataclass
from typing import Any

@dataclass
class Module:
    name: str
    typ: str
    dsts: list[str]
    recv: Any
    is_on: bool = False

    def send_signal(self, inp, recv_from):
        if self.typ == 'button':
            return False
        elif self.typ == 'broadcaster':
            return inp
        elif self.typ == 'f':
            if inp:
                return None
            self.is_on = not self.is_on
            return self.is_on
        elif self.typ == 'c':
            self.recv[recv_from] = inp
            return not all(self.recv.values())


def parse_dsts(dsts):
    if ',' not in dsts:
        return [dsts]
    else:
        return dsts.split(', ')


def parse_modules(inp):
    modules = {}
    modules['button'] = Module('button', 'button', ['broadcaster'], {})
    for line in inp:
        l, r = line.split(" -> ")
        dsts = parse_dsts(r)
        if l == 'broadcaster':
            dsts = parse_dsts(r)
            modules[l] = Module(l, 'broadcaster', dsts, {})
        elif l.startswith('%'):

            name = l[1:]
            modules[name] = Module(name, 'f', dsts, {})
        elif l.startswith('&'):
            # conjunction
            name = l[1:]
            modules[name] = Module(name, 'c', dsts, {})
   
    for k,v in modules.items():
        for d in v.dsts:
            if d not in modules:
                continue
            m = modules[d]
            if m.typ == 'c':
                m.recv[k] = False
    return modules


def solve1(inp):
    inp = inp.strip().split('\n')
    modules = parse_modules(inp)

    presses = 1000 
    lo, hi = 0, 0
    for i in range(presses):
        cur = [('button', False, '')]
        nxt = []
        while cur != []:
            for name, input_signal, recv_from in cur:
                if name not in modules:
                    continue
                m = modules[name]
                output_signal = m.send_signal(input_signal, recv_from)
                if output_signal is not None:
                    for d in m.dsts:
                        nxt.append((d, output_signal, name))
                    if output_signal:
                        hi += len(m.dsts)
                    else:
                        lo += len(m.dsts)
            cur = nxt
            nxt = []
    ans = lo * hi
    return ans 


def solve2(inp):
    inp = inp.strip().split('\n')
    modules = parse_modules(inp)
    
    presses = 0
    # Record latest hi signal for each input to mg
    latest = defaultdict(list)
    for i in range(100000):
        presses += 1
        cur = [('button', False, '')]
        nxt = []
        while cur != []:
            for name, input_signal, recv_from in cur:
                if name not in modules:
                    continue
                m = modules[name]
                if name == 'mg' and input_signal:
                    latest[recv_from].append(presses)
                output_signal = m.send_signal(input_signal, recv_from)
                if output_signal is not None:
                    for d in m.dsts:
                        nxt.append((d, output_signal, name))
            cur = nxt
            nxt = []
    cycle_sizes = []
    for k, t in latest.items():
        diffs = [j-i for i, j in zip(t[:-1], t[1:])]
        assert len(set(diffs)) == 1
        cycle_sizes.append(diffs[0])

    return lcm(*cycle_sizes)


example2 = """
broadcaster -> a
%a -> inv, con
&inv -> b
%b -> con
&con -> output
"""

if __name__=='__main__':
    example_ans = solve1(example)
    print(f'example 1:\n {example_ans}')
    assert example_ans == 32000000

    example_ans2 = solve1(example2)
    print(f'example 1-2:\n {example_ans2}')
    assert example_ans2 == 11687500

    actual_ans = solve1(actual)
    print(f'actual 1:\n {actual_ans}')

    actual_ans = solve2(actual)
    print(f'actual 2:\n {actual_ans}')

