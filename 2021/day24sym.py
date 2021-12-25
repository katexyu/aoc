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


from abc import ABC, abstractmethod
import sys


class Expression(ABC):
    @abstractmethod
    def simplify(self):
        pass

    @abstractmethod
    def iszero(self) -> bool:
        pass

    @abstractmethod
    def min(self) -> int:
        pass

    @abstractmethod
    def max(self) -> int:
        pass

    def __hash__(self):
        return hash(self.__repr__())

    def __eq__(self, other):
        return self.__repr__() == other.__repr__()

    def extract_input_eqn(self):
        return None, self


class Input(Expression):
    def __init__(self, idx):
        self.idx = idx

    def simplify(self) -> Expression:
        return self

    def __repr__(self):
        return f'IN[{self.idx}]'

    def iszero(self):
        return False
    
    def min(self):
        return 1
    
    def max(self):
        return 9
    

class Literal(Expression):
    def __init__(self, val):
        self.val = val
    
    def simplify(self) -> Expression:
        return self

    def __repr__(self):
        return f'{self.val}'

    def iszero(self):
        return self.val == 0

    def min(self):
        return self.val
    
    def max(self):
        return self.val


class Sum(Expression):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    @cache
    def simplify(self) -> Expression:
        left = self.left.simplify()
        right = self.right.simplify()

        if left.iszero():
            return right
        if right.iszero():
            return left
        if isinstance(left, Literal) and isinstance(right, Literal):
            return Literal(left.val + right.val)
        if isinstance(left, Sum) and isinstance(right, Literal):
            if isinstance(left.right, Literal):
                return Sum(left.left, Literal(left.right.val + right.val))
            if isinstance(left.left, Literal):
                return Sum(Literal(left.left.val + right.val), left.right)
        return Sum(left, right)

    def __repr__(self):
        return f'({self.left} + {self.right})'

    def iszero(self):
        return self.left.iszero() and self.right.iszero()

    def min(self):
        return self.left.min() + self.right.min()

    def max(self):
        return self.left.max() + self.right.max()


class Product(Expression):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    @cache
    def simplify(self) -> Expression:
        left = self.left.simplify()
        right = self.right.simplify()

        if left.iszero() or right.iszero():
            return Literal(0)
        elif isinstance(left, Literal) and isinstance(right, Literal):
            return Literal(left.val * right.val)
        elif isinstance(left, Literal) and left.val == 1:
            return right
        elif isinstance(right, Literal) and right.val == 1:
            return left
        if isinstance(right, Literal) and isinstance(left, Quotient):
            if left.right == right:
                return left.left
        return Product(left, right)
        

    def __repr__(self):
        return f'({self.left} * {self.right})'

    def iszero(self):
        return self.left.iszero() or self.right.iszero()

    def min(self):
        return self.left.min() * self.right.min()

    def max(self):
        return self.left.max() * self.right.max()


class Eq(Expression):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    @cache
    def simplify(self) -> Expression:
        left = self.left.simplify()
        right = self.right.simplify()

        if isinstance(left, Literal) and isinstance(right, Literal):
            return Literal(1) if left.val == right.val else Literal(0)
        if left.iszero() and right.iszero():
            return Literal(1)
        if self.left.max() < self.right.min() or self.left.min() > self.right.max():
            return Literal(0)
        return Eq(left, right)
        
    def __repr__(self):
        return f'({self.left} == {self.right})'

    def iszero(self):
        simplified = self.simplify()
        if simplified != self:
            return simplified.iszero()
        return False

    def min(self):
        return 0

    def max(self):
        return 1

    def extract_input_eqn(self):
        if isinstance(self.left, Input):
            return self, Literal(1)
        if isinstance(self.right, Input):
            return self, Literal(1)
        return None, self


class Quotient(Expression):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    @cache
    def simplify(self) -> Expression:
        left = self.left.simplify()
        right = self.right.simplify()
        
        if left.max() < right.min():
            return Literal(0)

        if isinstance(left, Literal) and isinstance(right, Literal):
            return Literal(left.val // right.val)

        if left.iszero():
            return Literal(0)

        if isinstance(right, Literal) and right.val == 1:
            return left

        if isinstance(left, Product):
            if left.left == right:
                return left.right
            elif left.right == right:
                return left.left
        if isinstance(self.left, Sum):
            return Sum(Quotient(self.left.left, self.right).simplify(), Quotient(self.left.right, self.right).simplify()).simplify()
        return Quotient(left, right)

    def __repr__(self):
        return f'({self.left} / {self.right})'

    def iszero(self):
        simplified = self.simplify()
        if simplified != self:
            return simplified.iszero()
        return False

    def min(self):
        return 0

    def max(self):
        return self.left.max()


class Mod(Expression):
    def __init__(self, left, modulus):
        self.left = left
        self.modulus = modulus

    @cache
    def simplify(self) -> Expression:
        left = self.left.simplify()
        modulus = self.modulus.simplify()
        if left.max() < modulus.min():
            return left

        if not isinstance(modulus, Literal):
            return Mod(left, modulus)

        if isinstance(left, Literal):
            return Literal(left.val % modulus.val)

        if isinstance(left, Product):
            if Mod(left.left, self.modulus).iszero() or Mod(left.right, modulus).iszero():
                return Literal(0)

        if isinstance(left, Sum):
            # Distribute the mod to both parts
            return Sum(Mod(left.left, modulus).simplify(), Mod(left.right, modulus).simplify()).simplify()
        return Mod(left, modulus)

    def __repr__(self):
        return f'({self.left} % {self.modulus})'


    def iszero(self):
        simplified = self.simplify()
        if simplified != self:
            return simplified.iszero()
        return False

    def min(self):
        return self.left.min() % self.modulus.min()

    def max(self):
        return self.modulus().max()


def solve(inp, find_min=False):
    inp = inp.strip().split('\n')
    inp = list(map(parse_line, inp))

    equality_conditions = extract_equality_conditions(inp)
    ranges = extract_ranges(equality_conditions)
    
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


def extract_ranges(input_eqns):
    range_map = {}
    for eqn in input_eqns:
        assert isinstance(eqn.left, Sum) and isinstance(eqn.right, Input)
        left_i = eqn.left.left.idx
        right_i = eqn.right.idx
        assert isinstance(eqn.left.right, Literal)
        diff = eqn.left.right.val

        valid_pairs = []
        for i in range(1, 10):
            i2 = i + diff
            if 1 <= i2 <= 9:
                valid_pairs.append((i, i2))
        assert len(valid_pairs) > 0
        range_map[left_i] = [valid_pairs[0][0], valid_pairs[-1][0]]
        range_map[right_i] = [valid_pairs[0][1], valid_pairs[-1][1]]

    return range_map
                
    
def extract_equality_conditions(inp):
    ops = []
    i = 0
    stored_vars = dict()
    equality_conditions = []
    for inst, args in inp:
        if inst == 'inp':
            var_name = args[0]
            stored_vars[var_name] = Input(i) 
            i += 1
        elif inst == 'add':
            arg1 = get_arg(args[0], stored_vars)
            arg2 = get_arg(args[1], stored_vars)
            var_name = args[0]
            stored_vars[var_name] = Sum(arg1, arg2).simplify() 
        elif inst == 'mul':
            arg1 = get_arg(args[0], stored_vars)
            arg2 = get_arg(args[1], stored_vars)
            var_name = args[0]
            stored_vars[var_name] = Product(arg1, arg2).simplify() 
        elif inst == 'div':
            arg1 = get_arg(args[0], stored_vars)
            arg2 = get_arg(args[1], stored_vars)
            var_name = args[0]
            stored_vars[var_name] = Quotient(arg1, arg2).simplify() 
        elif inst == 'mod':
            arg1 = get_arg(args[0], stored_vars)
            arg2 = get_arg(args[1], stored_vars)
            var_name = args[0]
            stored_vars[var_name] = Mod(arg1, arg2).simplify() 
        elif inst == 'eql':
            arg1 = get_arg(args[0], stored_vars)
            arg2 = get_arg(args[1], stored_vars)
            var_name = args[0]
            expr = Eq(arg1, arg2).simplify()
            # Try to extract an input equality that can be satisfied, and replace it in the register with a
            # Literal(1)
            input_eqn, val = expr.extract_input_eqn()
            if input_eqn is not None:
                equality_conditions.append(input_eqn.simplify())
            stored_vars[var_name] = val
        else:
            assert False, 'You should not get here'

    return equality_conditions


def get_arg(arg, stored_vars):
    if isinstance(arg, int):
        return Literal(arg)
    return stored_vars.get(arg, Literal(0))


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


def get_arg_value(stored_vars, arg):
    if isinstance(arg, int):
        return arg
    return stored_vars[arg]


if __name__=='__main__':
    max_ans = solve(actual)
    print(f'max:\n {max_ans}')

    min_ans = solve(actual, find_min=True)
    print(f'min:\n {min_ans}')



