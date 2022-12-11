from helpers import *
from collections import *
from itertools import *
from math import *
from heapq import heappush, heappop, heappushpop, heapify, heapreplace
from functools import cache
from dataclasses import dataclass
from typing import Callable, List


@dataclass
class Monkey:
    items: List[int]
    fn: Callable[[int], int]
    mod: int
    t: int
    f: int


# I started late and didn't feel like writing code to parse the input so I kind of just tried
# parsing the input by visual inspection today, which did lead to a handful of typos, but here you go
example = [
    Monkey(items=[79, 98], fn=lambda x:x*19, mod=23, t=2, f=3),
    Monkey(items=[54, 65, 75, 74], fn=lambda x:x+6, mod=19, t=2, f=0),
    Monkey(items=[79, 60, 97], fn=lambda x:x*x, mod=13, t=1, f=3),
    Monkey(items=[74], fn=lambda x:x+3, mod=17, t=0, f=1),
] 


actual = [
    Monkey(items=[66, 71, 94], fn=lambda x:x*5, mod=3, t=7, f=4),
    Monkey(items=[70], fn=lambda x:x+6, mod=17, t=3, f=0),
    Monkey(items=[62, 68, 56, 65, 94, 78], fn=lambda x:x+5, mod=2, t=3, f=1),
    Monkey(items=[89, 94, 94, 67], fn=lambda x:x+2, mod=19, t=7, f=0),
    Monkey(items=[71, 61, 73, 65, 98, 98, 63], fn=lambda x:x*7, mod=11, t=5, f=6),
    Monkey(items=[55, 62, 68, 61, 60], fn=lambda x:x+7, mod=5, t=2, f=1),
    Monkey(items=[93, 91, 69, 64, 72, 89, 50, 71], fn=lambda x:x+1, mod=13, t=5, f=2),
    Monkey(items=[76, 50], fn=lambda x:x*x, mod=7, t=4, f=6)
]


def solvea(monkeys):
    counts = [0 for i in monkeys]
    for i in range(20):
        for j, monkey in enumerate(monkeys):
            while len(monkey.items) > 0:
                counts[j] += 1
                item = monkey.items.pop(0)
                new_item = monkey.fn(item) // 3
                new_monkey = monkey.t if new_item % monkey.mod == 0 else monkey.f
                monkeys[new_monkey].items.append(new_item)

    s = sorted(counts)
    ans = s[-2] * s[-1]
    return ans 


def solve(monkeys):
    counts = [0 for m in monkeys]
    rounds = 10000

    modulo_product = prod(m.mod for m in monkeys)
    for i, monkey in enumerate(monkeys):
        for item in monkey.items:
            cur_monkey_idx = i
            cur_monkey = monkey
            cur = item
            cnt = rounds
            while cnt > 0:
                counts[cur_monkey_idx] += 1
                cur = cur_monkey.fn(cur) % modulo_product
                new_monkey_idx = cur_monkey.t if cur % cur_monkey.mod == 0 else cur_monkey.f
                if new_monkey_idx > cur_monkey_idx:
                    cnt += 1
                cur_monkey = monkeys[new_monkey_idx]
                cur_monkey_idx = new_monkey_idx
                cnt -= 1

    s = sorted(counts)
    ans = s[-2] * s[-1]
    return ans 


if __name__=='__main__':
    example_ans = solvea(example)
    print(f'example:\n {example_ans}')

    actual_ans = solvea(actual)
    print(f'actual:\n {actual_ans}')

    example_ans = solve(example)
    print(f'example:\n {example_ans}')

    actual_ans = solve(actual)
    print(f'actual:\n {actual_ans}')

