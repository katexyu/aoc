from helpers import *
from collections import *
from itertools import *
from math import *
from heapq import heappush, heappop, heappushpop, heapify, heapreplace
from functools import cache


example = """
inp w
add z w
mod z 2
div w 2
add y w
mod y 2
div w 2
add x w
mod x 2
div w 2
mod w 2
"""

actual = """
inp w
mul x 0
add x z
mod x 26
div z 1
add x 13
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 13
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 1
add x 11
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 10
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 1
add x 15
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 5
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 26
add x -11
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 14
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 1
add x 14
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 5
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 26
add x 0
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 15
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 1
add x 12
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 4
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 1
add x 12
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 11
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 1
add x 14
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 1
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 26
add x -6
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 15
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 26
add x -10
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 12
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 26
add x -12
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 8
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 26
add x -3
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 14
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 26
add x -5
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 9
mul y x
add z y
"""

"""
This problem was a real doozy. I tried brute forcing at first, which seemed like
it would take far too long. I then looked at the instructions and noticed that
it was repeating the same block of instructions with different arguments 14
times. I played around with various inputs and noticed that if you could get
the x value to equal w, then z would decrease in size for blocks with z div 26.
However, all blocks with `z div 1` would increase the z, so in order to solve
the problem, we need to match up any increase in z with a corresponding decrease
such that the final result is zero.
"""
def solve(inp, find_min=False):
    inp = inp.strip().split('\n')
    inp = list(map(parse_line, inp))

    blocks = parse_blocks(inp)
    stack = []
    ranges = dict()
    for b in blocks:
        if b.will_add():
            stack.append(b)
        else:
            # Try to match this block with the top of the stack
            b2 = stack.pop()
            b2_range, b_range = compute_block_match(b2, b)
            ranges[b2.idx] = b2_range
            ranges[b.idx] = b_range

    assert len(stack) == 0

    result = [] 
    for i in range(14):
        minw, maxw = ranges[i]
        if find_min:
            result.append(str(minw))
        else:
            result.append(str(maxw))
            
    # Verify that the input works
    assert process_alu(inp, result) == 0 

    return int(''.join(result))     


def compute_block_match(b1, b2):
    """
    b1 should have z_divisor=1 and b2 should have z_divisor=26
    """
    assert b1.will_add() and not b2.will_add()
    wz = []
    for w in range(1, 10):
        z = process_input(w, 0, b1.x_addend, b1.y_addend, b1.z_divisor)
        wz.append((w,z))

    viable_pairs = []
    for w, z in wz:
        for w2 in range(1, 10):
            result = process_input(w2, z, b2.x_addend, b2.y_addend, b2.z_divisor)
            if result == 0:
                viable_pairs.append((w, w2))

    if len(viable_pairs) == 0:
        raise f'Could not find a viable match between {b1.idx} and {b2.idx}'


    w1min, w2min = viable_pairs[0]
    w1max, w2max = viable_pairs[-1]

    return [w1min, w1max], [w2min, w2max]


class InstrBlock:
    def __init__(self, x_addend, y_addend, z_divisor, idx):
        self.x_addend = x_addend
        self.y_addend = y_addend
        self.z_divisor = z_divisor
        self.idx = idx

    def will_add(self):
        return self.z_divisor == 1


    def __repr__(self):
        return f'InstrBlock(x_addend={self.x_addend}, y_addend={self.y_addend}, z_divisor={self.z_divisor}, idx={self.idx})'


def parse_blocks(inp):
    blocks = []
    for i in range(14):
        args = inp[i*18:i*18+18]
        block = InstrBlock(args[5][1][1], args[15][1][1], args[4][1][1], i)
        blocks.append(block)
    return blocks


def get_arg_value(stored_vars, arg):
    if isinstance(arg, int):
        return arg
    if arg.isnumeric():
        return int(arg)
    return stored_vars[arg]


def parse_line(line):
    parts = line.split(' ')
    inst = parts[0]
    rest = []
    for x in range(1, len(parts)):
        i = parts[x]
        if i.isnumeric():
            rest.append(int(i))
        elif i[0] == '-':
            rest.append(int(i[1:]) * -1)
        else:
            rest.append(i)
    return (inst, rest)


def process_alu(instructions, inputs):
    i = 0
    stored_vars = defaultdict(int)
    for inst, args in instructions:
        if inst == 'inp':
            val = inputs[i]
            var_name = args[0]
            stored_vars[var_name] = int(val)
            i += 1
        elif inst == 'add':
            arg1 = get_arg_value(stored_vars, args[0])
            arg2 = get_arg_value(stored_vars, args[1])
            var_name = args[0]
            stored_vars[var_name] = arg1+arg2
        elif inst == 'mul':
            arg1 = get_arg_value(stored_vars, args[0])
            arg2 = get_arg_value(stored_vars, args[1])
            var_name = args[0]
            stored_vars[var_name] = arg1*arg2
        elif inst == 'div':
            arg1 = get_arg_value(stored_vars, args[0])
            arg2 = get_arg_value(stored_vars, args[1])
            var_name = args[0]
            stored_vars[var_name] = arg1 // arg2
        elif inst == 'mod':
            arg1 = get_arg_value(stored_vars, args[0])
            arg2 = get_arg_value(stored_vars, args[1])
            var_name = args[0]
            stored_vars[var_name] = arg1 % arg2
        elif inst == 'eql':
            arg1 = get_arg_value(stored_vars, args[0])
            arg2 = get_arg_value(stored_vars, args[1])
            var_name = args[0]
            stored_vars[var_name] = int(arg1 == arg2)
        else:
            assert False, 'You should not get here'
    ans = stored_vars['z']
    return ans


def process_input(w, z, x_addend, y_addend, z_divisor):
    """
    converting the block instructions to actual code 
    """
    x, y = 0, 0
    x = z
    x = x % 26
    z = z // z_divisor
    x += x_addend
    if x == w:
        y = 1
    else:
        y = 26
    z *= y
    y = w
    y += y_addend
    if x == w:
        y = 0    
    return z + y


# Some methods for manual checking
def z_div1_outputs(i):
    for j in range(1,10):
        z = process_input(j, 0, x_addends[i], y_addends[i], z_divisors[i])
        print(f'Got z: {z} for j = {j}')


def z_div26_outputs(i, zmin, zmax):
    for z in range(zmin, zmax+1):
        for j in range(1,10):
            result = process_input(j, z, x_addends[i], y_addends[i], z_divisors[i])
            if result == 0:
                print(f'Got result {result} for w={j}, z = {z}')


if __name__=='__main__':
    max_ans = solve(actual)
    print(f'max:\n {max_ans}')

    min_ans = solve(actual, find_min=True)
    print(f'min:\n {min_ans}')



