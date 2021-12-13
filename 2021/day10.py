from helpers import parse_lines

mapping = {
    ']': (57, '['),
    ')': (3, '('),
    '}': (1197, '{'),
    '>': (25137, '<'),
}

reverse = {
    '(': 1,
    '[': 2,
    '{': 3,
    '<': 4
}


def solve(data):
    scores = []
    for line in data:
        stack = []   
        skip = False
        for c in line:
            if c in ('[', '{', '<', '('):
                stack.append(c)
            else:
                s, left = mapping[c]
                if not stack or stack[-1] != left:
                    print(f'line: {line}, c: {c}, stack: {stack}, score: {s}, left: {left}')
                    skip = True
                    break
                else:
                    stack.pop()
        if skip:
            continue
        
        total = 0
        for c in reversed(stack):
            s = reverse[c]
            total = total * 5 + s
        scores.append(total)
     
    scores.sort()
        
    return scores[int(len(scores)/2)]


def get_data(filename='day10.txt'):
    return parse_lines(filename)


if __name__=='__main__':
    data = get_data()
    print(solve(data))

