from helpers import *
from collections import *
from itertools import *
from math import *
from heapq import heappush, heappop, heappushpop, heapify, heapreplace
from functools import cache


example = """
Sensor at x=2, y=18: closest beacon is at x=-2, y=15
Sensor at x=9, y=16: closest beacon is at x=10, y=16
Sensor at x=13, y=2: closest beacon is at x=15, y=3
Sensor at x=12, y=14: closest beacon is at x=10, y=16
Sensor at x=10, y=20: closest beacon is at x=10, y=16
Sensor at x=14, y=17: closest beacon is at x=10, y=16
Sensor at x=8, y=7: closest beacon is at x=2, y=10
Sensor at x=2, y=0: closest beacon is at x=2, y=10
Sensor at x=0, y=11: closest beacon is at x=2, y=10
Sensor at x=20, y=14: closest beacon is at x=25, y=17
Sensor at x=17, y=20: closest beacon is at x=21, y=22
Sensor at x=16, y=7: closest beacon is at x=15, y=3
Sensor at x=14, y=3: closest beacon is at x=15, y=3
Sensor at x=20, y=1: closest beacon is at x=15, y=3
"""

actual = """
Sensor at x=2692921, y=2988627: closest beacon is at x=2453611, y=3029623
Sensor at x=1557973, y=1620482: closest beacon is at x=1908435, y=2403457
Sensor at x=278431, y=3878878: closest beacon is at x=-1050422, y=3218536
Sensor at x=1432037, y=3317707: closest beacon is at x=2453611, y=3029623
Sensor at x=3191434, y=3564121: closest beacon is at x=3420256, y=2939344
Sensor at x=3080887, y=2781756: closest beacon is at x=3420256, y=2939344
Sensor at x=3543287, y=3060807: closest beacon is at x=3420256, y=2939344
Sensor at x=2476158, y=3949016: closest beacon is at x=2453611, y=3029623
Sensor at x=3999769, y=3985671: closest beacon is at x=3420256, y=2939344
Sensor at x=2435331, y=2200565: closest beacon is at x=1908435, y=2403457
Sensor at x=3970047, y=2036397: closest beacon is at x=3691788, y=1874066
Sensor at x=2232167, y=2750817: closest beacon is at x=2453611, y=3029623
Sensor at x=157988, y=333826: closest beacon is at x=-1236383, y=477990
Sensor at x=1035254, y=2261267: closest beacon is at x=1908435, y=2403457
Sensor at x=1154009, y=888885: closest beacon is at x=1070922, y=-543463
Sensor at x=2704724, y=257848: closest beacon is at x=3428489, y=-741777
Sensor at x=3672526, y=2651153: closest beacon is at x=3420256, y=2939344
Sensor at x=2030614, y=2603134: closest beacon is at x=1908435, y=2403457
Sensor at x=2550448, y=2781018: closest beacon is at x=2453611, y=3029623
Sensor at x=3162759, y=2196461: closest beacon is at x=3691788, y=1874066
Sensor at x=463834, y=1709480: closest beacon is at x=-208427, y=2000000
Sensor at x=217427, y=2725325: closest beacon is at x=-208427, y=2000000
Sensor at x=3903198, y=945190: closest beacon is at x=3691788, y=1874066
"""

from dataclasses import dataclass

@dataclass
class SensorInfo:
    x: int
    y: int
    beacon_x: int
    beacon_y: int
    dist: int = None

    def __post_init__(self):
        self.dist = dist(self.x, self.y, self.beacon_x, self.beacon_y)
 

def parse_line(l):
    parts = l.split(' ')
    x = int(parts[2].split('=')[1][:-1])
    y = int(parts[3].split('=')[1][:-1])
    beacon_x = int(parts[8].split('=')[1][:-1])
    beacon_y = int(parts[9].split('=')[1])
    return SensorInfo(
        x,
        y,
        beacon_x,
        beacon_y
    )


def solve(inp, line=10):
    inp = inp.strip().split('\n')
    sensor_info = list(map(parse_line, inp))
    minx = min(min(si.x, si.beacon_x) for si in sensor_info)
    maxx = max(max(si.x, si.beacon_x) for si in sensor_info)
    beacons = set((si.beacon_x, si.beacon_y) for si in sensor_info)

    cnt = 0
    for x in range(minx*2, maxx*2):
        # check if a beacon can be closer than an existing one
        y = line
        for si in sensor_info:
            if (x, y) in beacons:
                break
            if dist(si.x, si.y, x, y) <= si.dist:
                cnt += 1
                break
    return cnt

def solveb(inp, maxval=20):
    inp = inp.strip().split('\n')
    sensor_info = list(map(parse_line, inp))
    minx = min(min(si.x, si.beacon_x) for si in sensor_info)
    maxx = max(max(si.x, si.beacon_x) for si in sensor_info)
    beacons = set((si.beacon_x, si.beacon_y) for si in sensor_info)

    ranges = []

    for y in range(0, maxval):
        ranges = sorted(list(filter(lambda x: x is not None, (range_from_beacon(si, y) for si in sensor_info))))
        if len(ranges) == 1:
            continue
        merged = merge_ranges(ranges)
        if len(merged) > 1:
            # find where the range does not overlap
            x = merged[0][1] + 1
            
            return x * 4000000 + y


def merge_ranges(ranges):
    merged = []
    current = ranges[0]
    for r in ranges[1:]:
        if overlaps(current, r):
            current = (min(current[0], r[0]), max(current[1], r[1]))
        else:
            merged.append(current)
            current = r

    merged.append(current)
    return merged

def range_from_beacon(si, y):
    d = abs(si.y - y)
    if d > si.dist:
        return None
    dx = si.dist - d
    return (si.x - dx, si.x + dx)


def overlaps(r1, r2):
    return not (r1[1] < r2[0] or r1[0] > r2[1])    


def dist(x1, y1, x2, y2):
    return abs(x1-x2) + abs(y1-y2)


if __name__=='__main__':
    #example_ans = solve(example, 10)
    #print(f'example:\n {example_ans}')

    #actual_ans = solve(actual,2000000)
    #print(f'actual:\n {actual_ans}')

    example_ans = solveb(example, 20)
    print(f'example:\n {example_ans}')

    actual_ans = solveb(actual, 4000000)
    print(f'actual:\n {actual_ans}')


