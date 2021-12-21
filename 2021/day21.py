from helpers import *
from collections import *
from itertools import *
from math import *
from heapq import heappush, heappop, heappushpop, heapify, heapreplace
from functools import cache


example = [4, 8] 

actual = [2, 5]


class Die:
    def __init__(self):
        self.turns = 0

    def roll(self):
        self.turns += 1
        if self.turns > 100:
            self.turns = 1
        return self.turns
    

def solve(inp):
    die = Die()
    p1, p2 = inp

    pts1 = 0
    pts2 = 0
    turn = True
    while pts1 < 1000 and pts2 < 1000:
        if turn:
            p1 += die.roll() + die.roll() + die.roll() 
            p1 = (p1-1) % 10 + 1
            pts1 += p1
        else:
            p2 += die.roll() + die.roll() + die.roll() 
            p2 = (p2-1) % 10 + 1
            pts2 += p2
        turn = not turn
    loser = min(pts1, pts2)
    print(loser)
    print(die.turns)
    return loser * die.turns


def solveb(inp):
    # What I actually used to get an answer, takes ~25s
    p1, p2 = inp

    pts1 = 0
    pts2 = 0
    p1_turn = True
    count1 = 0
    count2 = 0

    queue = deque([(pts1, pts2, p1, p2, p1_turn, 1)])
    step_values = Counter([sum(p) for p in product([1,2,3], [1,2,3], [1,2,3])])
    threshold = 21
    while queue:
        pts1, pts2, p1, p2, p1_turn, factor = queue.popleft()
        if p1_turn:
            for steps, count in step_values.items():
                np1 = do_step(p1, steps)
                npts1 = pts1 + np1
                if npts1 >= threshold:
                    count1 += count * factor
                else:
                    queue.append((npts1, pts2, np1, p2, False, count * factor))
        else:
            for steps, count in step_values.items():
                np2 = do_step(p2, steps)
                npts2 = pts2 + np2
                if npts2 >= threshold:
                    count2 += count * factor
                else:
                    queue.append((pts1, npts2, p1, np2, True, count * factor))
        
    print(f'1: {count1} | 2: {count2}')
    return max(count1, count2)


@cache
def do_step(p, d):
    p += d
    p = (p-1) % 10 + 1
    return p


def solveb_better(inp):
    """
    8-9x faster than solveb by caching more of the work
    """
    p1, p2 = inp

    threshold = 21
    counts = do_turn(0, 0, p1, p2, True, 1, threshold)

    print(counts)
    return max(counts)


step_counts = Counter([sum(p) for p in product([1,2,3], [1,2,3], [1,2,3])])


@cache
def do_turn(pts1, pts2, p1, p2, p1_turn, factor, threshold):
    counts = [0, 0]
    if p1_turn:
        for steps, count in step_counts.items():
            np1 = do_step(p1, steps)
            npts1 = pts1 + np1
            if npts1 >= threshold:
                counts[0] += count * factor
            else:
                c1, c2 = do_turn(npts1, pts2, np1, p2, False, count * factor, threshold)
                counts[0] += c1
                counts[1] += c2
    else:
        for steps, count in step_counts.items():
            np2 = do_step(p2, steps)
            npts2 = pts2 + np2
            if npts2 >= threshold:
                counts[1] += count * factor
            else:
                c1, c2 = do_turn(pts1, npts2, p1, np2, True, count * factor, threshold)
                counts[0] += c1
                counts[1] += c2
    return counts



if __name__=='__main__':
    example_ans = solveb_better(example)
    print(f'example:\n {example_ans}')

    actual_ans = solveb_better(actual)
    print(f'actual:\n {actual_ans}')

