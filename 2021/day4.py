from collections import defaultdict
from math import floor

def solve(numbers, boards):
    mapping = defaultdict(list)
    for b in boards:
        for i in range(len(b)):
            for j in range(len(b[0])):
                val = b[i][j]
                mapping[val].append(b)

    winner = None
    winning_num = 0

    done = False
    for n in numbers:
        mboards = mapping[n]
        for b in mboards:
            update_board(b, n)
            done = check_done(b)
            if done:
                winner = b
                winning_num = n
                break
        if done:
            break
    
    print(f'winner: {winner}')
    unmarked_sum = 0
    for i in range(len(winner)):
        for j in range(len(winner[0])):
            if winner[i][j] != 'x':
                unmarked_sum += winner[i][j]

    return unmarked_sum * winning_num


def solveb(numbers, boards):
    mapping = defaultdict(list)
    for idx, b in enumerate(boards):
        for i in range(len(b)):
            for j in range(len(b[0])):
                val = b[i][j]
                mapping[val].append(idx)

    done = [False] * len(boards)

    last_board = None
    last_num = 0

    for n in numbers:
        mboards = mapping[n]
        for bidx in mboards:
            b = boards[bidx]
            update_board(b, n)
            last_num = n
            if not done[bidx]:
                d = check_done(b)
                if d:
                    done[bidx] = True
                    if all(done):
                        last_board = boards[bidx]
                        break
        if all(done):
            break
    
    unmarked_sum = 0
    for i in range(len(last_board)):
        for j in range(len(last_board[0])):
            if last_board[i][j] != 'x':
                unmarked_sum += last_board[i][j]

    return unmarked_sum * last_num


def update_board(b, n):
    for i in range(len(b)):
        for j in range(len(b[0])):
            if b[i][j] == n:
                b[i][j] = 'x'
                return


def check_done(b):
    # check all rows first
    for i in range(len(b)):
        done = True

        for j in range(len(b[0])):
            if b[i][j] != 'x':
                done = False
        if done:
            return True

    # check all columns
    for j in range(len(b[0])):
        done = True
        for i in range(len(b)):
            if b[i][j] != 'x':
                done = False
        if done:
            return True
    return False
                  

def format_board(b):
    return '\n'.join(('').join(str(bb)) for bb in b)


def get_data(filename='day4.txt'):
    with open(filename, 'r') as f:
        lines = f.readlines()
        numbers = [int(i) for i in lines[0].split(',')]
        boards = []
        for i in range(floor((len(lines))/6)):
            board = [
                [int(num) for num in lines[j].strip(' ').split(' ') if num != '']
                for j in range(i*6+2, i*6+7)
            ]
            boards.append(board)
        
        return numbers, boards


if __name__=='__main__':
    numbers, boards = get_data()

    #print(solve(numbers, boards))
    print(solveb(numbers, boards))
