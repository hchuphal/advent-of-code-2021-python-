# day2 AOC 2021
def main():
    horizontal = depth = 0
    horizontal2 = depth2 = aim= 0
    for line in open('day2_data.txt'):
        command, value = line.split()
        if command == 'forward':
            horizontal += int(value) 
            horizontal2 += int(value)
            depth2 += int(value) * aim
        elif command == 'up':
            depth -= int(value)
            aim -= int(value)
        else:
            #command == 'down'
            depth += int(value)
            aim += int(value)

    part1 = horizontal * depth
    part2 = horizontal2 * depth2
    return part1, part2

if __name__== "__main__":
    r1, r2 = main()
    print("Result part1 : {} and part2 : {}".format(r1, r2))
