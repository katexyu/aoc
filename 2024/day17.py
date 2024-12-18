from helpers import *
from collections import *
from itertools import *
from math import *
from heapq import heappush, heappop, heappushpop, heapify, heapreplace
from functools import cache


def op_val(operand, a, b, c):
    if operand <= 3:
        return operand
    if operand == 4:
        return a
    if operand == 5:
        return b
    if operand == 6:
        return c


def run_program(a, program, should_match = False):
    outputs = []
    pointer, b, c = 0, 0, 0
    while pointer < len(program):
        op = program[pointer]
        lit_operand = program[pointer+1]
        combo_operand = op_val(lit_operand, a, b, c)
        if op == 0:
            d = 2 ** combo_operand
            a = a // d
        elif op == 1:
            b = b ^ lit_operand
        elif op == 2:
            b = combo_operand % 8
        elif op == 3:
            if a != 0:
                pointer = lit_operand
                continue
        elif op == 4:
            b = b ^ c
        elif op == 5:
            outputs.append(combo_operand % 8)
            if should_match:
                if outputs != program[:len(outputs)]:
                    return outputs
        elif op == 6:
            d = 2 ** combo_operand
            b = a // d
        elif op == 7:
            d = 2 ** combo_operand
            c = a // d
        pointer += 2

    return outputs


def solve1(a, program):
    outputs = run_program(a, program)
    return ','.join([str(x) for x in outputs])



def solve2(program):
    tot = 0
    for i in range(1, len(program)+1):
        target = program[len(program)-i:]
        for a in range(8*8):
            output = run_program(tot+a, program)
            if output == target:
                tot += a
                break
        tot <<=3

    # We've shifted an extra 3 bits, so shift back
    tot >>= 3
    assert run_program(tot, program) == program
    return tot


if __name__=='__main__':
    example_ans = solve1(729, [0,1,5,4,3,0])
    print(f'example 1:\n {example_ans}')

    actual_ans = solve1(38610541, [2,4,1,1,7,5,1,5,4,3,5,5,0,3,3,0])
    print(f'actual 1:\n {actual_ans}')

    example_ans = solve2([0,3,5,4,3,0])
    print(f'example 2:\n {example_ans}')

    actual_ans = solve2([2,4,1,1,7,5,1,5,4,3,5,5,0,3,3,0])
    print(f'actual 2:\n {actual_ans}')

