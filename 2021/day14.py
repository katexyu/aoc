from helpers import *
from collections import defaultdict


def solve(template, rules, num_rounds):
    counts = defaultdict(int)
    for i in range(len(template)-1):
        pair = template[i:i+2]
        counts[pair] += 1

    for i in range(num_rounds):
        new_counts = defaultdict(int)
        for pair in counts:
            insertion = rules[pair]
            left = pair[0] + insertion
            right = insertion + pair[1]
            new_counts[left] += counts[pair]
            new_counts[right] += counts[pair]
        counts = new_counts
    return get_count_difference(counts, template[0], template[-1])


def get_count_difference(counts, left, right):
    c = defaultdict(int)
    for pair, v in counts.items():
        c[pair[0]] += v
        c[pair[1]] += v

    # Add back the ends, since they are only covered by 1 pair each
    c[left] += 1
    c[right] += 1

    vals = sorted(c.values())
    return (vals[-1] - vals[0]) / 2


def get_data(filename='day14.txt'):
    lines = parse_lines(filename)
    template = lines[0]
    rules = dict()
    for l in range(2, len(lines)):
        line = lines[l]
        parts = line.split(' -> ')
        rules[parts[0]] = parts[1]
    return template, rules


if __name__=='__main__':
    example_template, example_rules = get_data('day14a.txt')
    assert(solve(example_template, example_rules, 10) == 1588)
    assert(solve(example_template, example_rules, 40) == 2188189693529)

    template, rules = get_data()
    soln = solve(template, rules, 10)
    print(f'Part a: {soln}')
    solnb = solve(template, rules, 40)
    print(f'Part b: {solnb}')

