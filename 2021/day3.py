from helpers import parse_digits_grid


def solve(data):
    l = len(data)
    h = len(data[0])

    gammab = []
    epsilonb = []

    for i in range(h):
        s = sum(line[i] for line in data)
        if s > l/2:
            gammab.append(1)
            epsilonb.append(0)
        else:
            gammab.append(0)
            epsilonb.append(1)

    gamma = compute_binary(gammab)
    epsilon = compute_binary(epsilonb)
    return gamma * epsilon


def solveb(data):
    l = len(data)
    h = len(data[0])

    gammab = []
    epsilonb = []

    oxyb = data
    co2b = data

    for i in range(h):
        so = sum(line[i] for line in oxyb)
        mcd = 1 if so >= len(oxyb)/2 else 0

        oxyb = [o for o in filter(lambda x: x[i] == mcd, oxyb)]
        
        sc = sum(line[i] for line in co2b)
        lcd = 1 if sc < len(co2b)/2 else 0
        if len(co2b) > 1:
            co2b = [c for c in filter(lambda x: x[i] == lcd, co2b)]
            
    oxy = compute_binary(oxyb[0])
    co2 = compute_binary(co2b[0]) 
    return oxy * co2


def compute_binary(arr):
    total = 0
    for i, val in enumerate(reversed(arr)):
        total += val << i
    return total


def get_data(filename='day3.txt'):
    return parse_digits_grid(filename)


if __name__=='__main__':
    data = get_data()
    print(solve(data))
    print(solveb(data))
