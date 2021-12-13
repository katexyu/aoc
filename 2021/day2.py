def read_data(filename='day2.txt'):
    with open(filename, 'r') as f:
        return f.readlines()


def parse_data(arr):
    return [parse_line(a) for a in arr]


def parse_line(line):
    cleaned = line.strip("\n")
    parts = cleaned.split(" ")
    num = int(parts[1])
    direction = parts[0]
    if direction == 'forward':
        return (num, 0)
    if direction == 'up':
        return (0, num * -1)
    if direction == 'down':
        return (0, num)


def compute_coordinates(parsed_data):
    pos = sum(d[0] for d in parsed_data)
    depth = sum(d[1] for d in parsed_data)
    return pos * depth

 
def compute_part2(parsed_data):
    aim = 0
    pos = 0
    depth = 0
    for a, b in parsed_data:
        if a != 0:
            pos += a
            depth += a * aim
        else:
            aim += b

    return pos * depth
        
    
if __name__=='__main__':
    data = read_data()
    parsed = parse_data(data)
    print(f"result was {compute_coordinates(parsed)}")
    print(f"result was {compute_part2(parsed)}")

