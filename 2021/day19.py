from helpers import *
from collections import *
from itertools import *
from math import *
from heapq import heappush, heappop, heappushpop, heapify, heapreplace
from functools import cache


example = 'day19e.txt' 

actual = 'day19.txt'

example_coords = """
-618,-824,-621
-537,-823,-458
-447,-329,318
404,-588,-901
544,-627,-890
528,-643,409
-661,-816,-575
390,-675,-793
423,-701,434
-345,-311,381
459,-707,401
-485,-357,347
"""

THRESHOLD = 66 # 12 c 2


def parse_example():
    inp = example_coords.strip().split('\n')
    coords = []
    for i in inp:
        raw = list(map(int, i.split(',')))
        coords.append(raw)
    diffs = diffs_between_coords(coords)
    return diffs


def solve(inp):
    inp = parse_lines(inp)
    mapping = defaultdict(list)
    current = None
    for i in inp:
        if i.startswith('---'):
            current = int(i.split(' ')[2])
        elif len(i) > 0:
            coordinates = list(map(int, i.split(',')))
            mapping[current].append(coordinates)

    scanners = list(mapping.keys())
    first = scanners[0]

    distances = dict()
    distances[first] = diffs_between_coords(mapping[first])
    overlaps = set()

    adjacent = defaultdict(list)

    # Kind of janky, but do this so we can figure out an dependency graph
    # for an order to process scanners in
    for s in combinations(scanners, 2):
        s1 = min(s)
        s2 = max(s)
        d1 = diffs_between_coords(mapping[s1])
        result, _, _, _ = overlap_with(d1, s2, mapping)
        if result:
            adjacent[s1].append(s2)
            adjacent[s2].append(s1)

    # We need to make sure we process scanners in an order that makes sense
    # in order to orient them correctly
    queue = deque([first])
    visited = set([first])
    coords = set()
    coords.update(map(tuple, mapping[first]))

    positions = [(0, 0, 0)] 
    while queue:
        cur = queue.popleft()
        neighbors = adjacent[cur]
        if cur != first:
            s1 = None
            # Find a predecessor that has already been visited and translated to the
            # first scanner's coordinate system
            for n in neighbors:
                if n in distances:
                    s1 = n
                    break
            assert s1 is not None
            d = distances[s1]
            result, oriented_differences, cur_coords, location = overlap_with(d, cur, mapping)
            coords.update(cur_coords)
            positions.append(location)
            distances[cur] = oriented_differences
        for n in neighbors:
            if n not in visited:
                queue.append(n)
                visited.add(n)

    print(f'Number of beacons: {len(coords)}')

    max_dist = 0
    for x, y in combinations(positions, 2):
        diff = diff_coordinates(x, y)
        manhattan = abs(diff[0]) + abs(diff[1]) + abs(diff[2])
        max_dist = max(manhattan, max_dist)

    return max_dist 


@cache
def orientations():
    xyz = {0, 1, 2}
    out = []
    for elem in xyz:
        for e in xyz - {elem}:
            out.extend([[1, elem, 1, e], [-1, elem, 1, e], [1, elem, -1, e], [-1, elem, -1, e]])
    return out


def map_orientation(c, o, remaining_sign):
    sign_facing, facing_axis, sign_up, up_axis = o
    x1 = c[facing_axis] * sign_facing
    z1 = c[up_axis] * sign_up

    (y,) = {0, 1, 2} - {facing_axis, up_axis}
    y1 = c[y] * remaining_sign
    return [x1, y1, z1]
    

def overlap_with(s1_distances, s2, mapping):
    coords = mapping[s2]
    for o in orientations():
        for s in [1, -1]:
            mapped_coords = [map_orientation(c, o, s) for c in coords]
            s2_distances = diffs_between_coords(mapped_coords)
            overlaps = find_overlaps(s1_distances, s2_distances)
            
            if len(overlaps) >= THRESHOLD:
                diff = None
                diff_prev = None
                should_return = True
                
                # Make sure that the diffs don't just happen to match and
                # that there's a consistent diff
                for ov in overlaps:
                    c1_start, c1_end = s1_distances[ov]
                    c2_start, c2_end = s2_distances[ov]
                    diff = diff_coordinates(c2_start, c1_start)
                    diff2 = diff_coordinates(c2_end, c1_end)
                    assert diff == diff2
                    if diff_prev is not None and diff_prev != diff:
                        should_return = False
                        break
                    diff_prev = diff
                assert diff is not None
                
                if should_return:
                    ret_coords = translate_coords(mapped_coords, diff)

                    for k in s2_distances:
                        s2_distances[k] = translate_coords(s2_distances[k], diff)
                    return overlaps, s2_distances, ret_coords, diff
    return [], None, None, None


def translate_coords(coords, diff):
   return [translate(c, diff) for c in coords] 


def find_overlaps(c1, c2):
    s1 = set(c1)
    s2 = set(c2)
    overlaps = s1.intersection(s2)
    return overlaps


def diffs_between_coords(coords):
    # Returns a map of diffs to the coordinates that produced the diff
    distances = {}
    for subset in combinations(coords, 2):
        l = max(subset)
        s = min(subset)
        dist = diff_coordinates(s, l)
        distances[dist] = (l, s) 
    return distances


def diff_coordinates(x, y):
    return (y[0] - x[0], y[1] - x[1], y[2] - x[2])


def translate(c, diff):
    return (c[0] + diff[0], c[1] + diff[1], c[2] + diff[2])


if __name__=='__main__':
    example_ans = solve(example)
    print(f'example:\n {example_ans}')

    actual_ans = solve(actual)
    print(f'actual:\n {actual_ans}')

