from helpers import *
from collections import *
from itertools import *
from math import *
from heapq import heappush, heappop, heappushpop, heapify, heapreplace
from functools import cache


example = r"""
x00: 1
x01: 1
x02: 1
y00: 0
y01: 1
y02: 0

x00 AND y00 -> z00
x01 XOR y01 -> z01
x02 OR y02 -> z02
"""

example2 = r"""
x00: 1
x01: 0
x02: 1
x03: 1
x04: 0
y00: 1
y01: 1
y02: 1
y03: 1
y04: 1

ntg XOR fgs -> mjb
y02 OR x01 -> tnw
kwq OR kpj -> z05
x00 OR x03 -> fst
tgd XOR rvg -> z01
vdt OR tnw -> bfw
bfw AND frj -> z10
ffh OR nrd -> bqk
y00 AND y03 -> djm
y03 OR y00 -> psh
bqk OR frj -> z08
tnw OR fst -> frj
gnj AND tgd -> z11
bfw XOR mjb -> z00
x03 OR x00 -> vdt
gnj AND wpb -> z02
x04 AND y00 -> kjc
djm OR pbm -> qhw
nrd AND vdt -> hwm
kjc AND fst -> rvg
y04 OR y02 -> fgs
y01 AND x02 -> pbm
ntg OR kjc -> kwq
psh XOR fgs -> tgd
qhw XOR tgd -> z09
pbm OR djm -> kpj
x03 XOR y03 -> ffh
x00 XOR y04 -> ntg
bfw OR bqk -> z06
nrd XOR fgs -> wpb
frj XOR qhw -> z04
bqk OR frj -> z07
y03 OR x01 -> nrd
hwm AND bqk -> z03
tgd XOR rvg -> z12
tnw OR pbm -> gnj
"""

with open('day24.txt', 'r') as f:
    actual = f.read()

with open('day24fixed.txt', 'r') as f:
    fixed = f.read()


from dataclasses import dataclass
from typing import Callable, Optional
from abc import ABC, abstractmethod


@dataclass
class Gate(ABC):
    left: str
    right: str
    out: str
    computed: bool
    identifier: str
    func: Callable[[int, int], int]

    def is_computed(self):
        return self.computed

    def can_be_computed(self, m):
        return self.left in m and self.right in m

    def compute(self, l, r):
        return self.func(l, r)

    def compute_and_set(self, m):
        m[self.out] = self.compute(m[self.left], m[self.right])
        self.computed = True


def toposort_recursive(w, deps, visited, stack):
    visited[w] = True
    for g in deps[w]:
        if visited[g.out] == False:
            toposort_recursive(g.out, deps, visited, stack)
    stack.insert(0, w)


def toposort(wires, deps):
    visited = defaultdict(bool)
    stack = []
    for w in wires:
        if not visited[w]:
            toposort_recursive(w, deps, visited, stack)
    return stack


def propagate(w, deps, wires):
    gates = deps[w]
    for g in gates:
        if g.can_be_computed(wires):
            g.compute(wires)


def solve1(inp):
    inp = inp.strip().split('\n\n')
    vals = inp[0].split('\n')
    wires = dict()
    for v in vals:
        l, r = v.split(': ')
        wires[l] = int(r)

    gates = []
    raw_gates = inp[1].split('\n')


    deps = defaultdict(list)
    count = defaultdict(int)

    z_wires = set()
    all_wires = set()
    for r in raw_gates:
        tokens = r.split(' ')
        l, operator, r, _, out = tokens
        all_wires.update([l, r, out])
        func = None
        if operator == 'AND':
            t = 'AND'
            func = lambda x,y: x & y
        if operator == 'OR':
            t = 'OR'
            func = lambda x,y: x | y
        if operator == 'XOR':
            t = 'XOR'
            func = lambda x,y: x ^ y
        identifier = f"{t}{count[t]}"
        count[t] += 1
        gates.append(Gate(l,r,out,False, identifier, func))
        last_gate = gates[-1]
        deps[l].append(last_gate)
        deps[r].append(last_gate)
        if out.startswith('z'):
            z_wires.add(out)

    order = toposort(all_wires, deps)

    for w in order:
        gates = deps[w]
        for g in gates:
            if g.can_be_computed(wires):
                g.compute_and_set(wires)
    
    return compute_num(wires, z_wires)


def compute_num(wires, val_wires):
    total = 0
    for i, w in enumerate(reversed(sorted(val_wires))):
        total += wires[w]
        total <<= 1
    return total >> 1


import graphviz


def solve2(inp):
    inp = inp.strip().split('\n\n')
    vals = inp[0].split('\n')
    wires = dict()
    y_vals = set()
    x_vals = set()
    dot = graphviz.Digraph(comment='Gate dependency graph')
    for v in vals:
        l, r = v.split(': ')
        wires[l] = int(r)
        if l[0] == 'x':
            dot.node(l, f'X input {l}')
            x_vals.add(l)
        if l[0] == 'y':
            dot.node(l, f'Y input {l}')
            y_vals.add(l)

    x, y = compute_num(wires, x_vals), compute_num(wires, y_vals)
    expected_z_numerical = x + y
    expected_z_bits = [0 for i in range(46)]
    for i in range(46):
        expected_z_bits[i] = (expected_z_numerical >> i) & 1

    gates = []
    raw_gates = inp[1].split('\n')

    deps = defaultdict(list)
    output_to_gate = dict()

    z_wires = set()
    all_wires = set()
    out_gate_mapping = dict()
    count = defaultdict(int)

    for r in raw_gates:
        tokens = r.split(' ')
        l, operator, r, _, out = tokens
        all_wires.update([l, r, out])
        func = None
        if operator == 'AND':
            t = 'AND'
            func = lambda x,y: x & y
        if operator == 'OR':
            t = 'OR'
            func = lambda x,y: x | y
        if operator == 'XOR':
            t = 'XOR'
            func = lambda x,y: x ^ y
        identifier = f"{t}{count[t]}"
        count[t] += 1
        gates.append(Gate(l,r,out,False,identifier, func))
        out_gate_mapping[out] = identifier
        last_gate = gates[-1]
        deps[l].append(last_gate)
        deps[r].append(last_gate)
        output_to_gate[out] = last_gate

        if out.startswith('z'):
            z_wires.add(out)

    non_matching_outputs = []

    print(f"x+y=z is {check_deps(all_wires, wires, deps, x, y, z_wires)}")

    for i, zw in enumerate(sorted(z_wires)):
        zval = wires[zw]
        if zval != expected_z_bits[i]:
            print(f"zval {zval} for zw={zw} did not match expected at idx={i}")
            non_matching_outputs.append(zw)
    print(f"non_matching_outputs: {non_matching_outputs}")

    for g in gates:
        left = out_gate_mapping.get(g.left, g.left)
        right = out_gate_mapping.get(g.right, g.right)
        dot.node(g.identifier, f"{g.identifier}-{g.out}-{wires[g.out]}" )
        dot.edge(left, g.identifier)
        dot.edge(right, g.identifier)

    # Graphed the dependency tree and identified swaps by visual inspection

    # dot.render('doctest-output/day24.gv', view=True)  # doctest: +SKIP
    # 'doctest-output/day24.gv.pdf'

def check_deps(all_wires, wires, deps, x, y, z_wires):
    order = toposort(all_wires, deps)
    for w in order:
        gates = deps[w]
        for g in gates:
            if g.can_be_computed(wires):
                g.compute_and_set(wires)
    z = compute_num(wires, z_wires)
    print(f"x={x}, y={y}, z={z}")

    return x + y == z


if __name__=='__main__':
    example_ans = solve1(example)
    print(f'example 1:\n {example_ans}')

    actual_ans = solve1(actual)
    print(f'actual 1:\n {actual_ans}')

    print(f'Trying actual input for part 2...')
    solve2(actual)
    print(f'Trying fixed input for part 2...')
    solve2(fixed)


