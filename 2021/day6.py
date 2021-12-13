from collections import defaultdict
from math import floor
from helpers import parse_csv_grid

def solve(fish, days):
    counts = defaultdict(int)
    for f in fish:
        counts[f] += 1

    for i in range(days):
        new_fish = counts[0]
        for x in range(1, 9):
            counts[x-1] = counts[x]
            counts[x] = 0

        counts[6] += new_fish
        counts[8] = new_fish
            
    return sum(counts.values())    

    
def get_data(filename='day6.txt'):
    return parse_csv_grid(filename)[0]
        

if __name__=='__main__':
    fish = get_data()

    print(solve(fish, 80))
    print(solve(fish, 256))
