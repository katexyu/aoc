from collections import defaultdict
from math import floor


MAPPING = {
    0: 'abcefg',
    1: 'cf',
    2: 'acdeg',
    3: 'acdfg',
    4: 'bcdf',
    5: 'abdfg',
    6: 'abdefg',
    7: 'acf',
    8: 'abcdefg',
    9: 'abcdfg',
}

def solve(data):
    times = 0
    for x, out in data:
        for seq in out:
            if len(seq) in (2, 3, 4, 7):
                times += 1
    return times


def solveb(data):
    out = 0
    for x, y in data:
        x = [''.join(sorted(a)) for a in x]
        x.sort(key=lambda f: len(f))

        y = [''.join(sorted(a)) for a in y]
        mapping = find_mapping(x)
        number = mapping[y[0]] * 1000 + mapping[y[1]] * 100 + mapping[y[2]] * 10 + mapping[y[3]]
        out += number
    return out
        

def find_mapping(left):
    mapping = dict()
    solved = set()
    print(left)
    mapping[1] = left[0]
    mapping[7] = left[1]
    mapping[4] = left[2]
    mapping[8] = left[-1]

    zerosixnine = [l for l in left if len(l) == 6]
    six = [l for l in zerosixnine if not set(mapping[7]).issubset(l)][0]
    zerosixnine.remove(six)
    nine = [l for l in zerosixnine if set(mapping[4]).issubset(l)][0]
    zerosixnine.remove(nine)
    zero = zerosixnine[0]
    mapping[6] = six
    mapping[9] = nine
    mapping[0] = zero


    twothreefive = [l for l in left if len(l) == 5]
    three = [l for l in twothreefive if set(mapping[7]).issubset(l)][0]
    twothreefive.remove(three)
    mapping[3] = three

    five = [l for l in twothreefive if set(l).issubset(mapping[6])][0]
    twothreefive.remove(five)
    mapping[5] = five
    mapping[2] = twothreefive[0]
    print(mapping)    
    reverse_mapping = dict()
    for k,v in mapping.items():
        reverse_mapping[v] = k
    return reverse_mapping


def get_data(filename='day8.txt'):
    out = []
    with open(filename, 'r') as f:
        lines = f.readlines()
        for l in lines:
            parts = l.strip('\n').split(' | ')
            left = parts[0].split(' ')
            right = parts[1].split(' ')
            out.append([left, right])
        return out        


if __name__=='__main__':
    data = get_data()

    print(solveb(data))

