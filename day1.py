# day1 AOC 2021
def main(part1, part2):
    input = [int(n) for n in open('day1_data.txt')]
    for i in range(len(input)):
        if i >= 1 and input[i] > input[i-1]:
            part1 += 1
        if i >= 3: 
            if input[i]+input[i-1]+input[i-2] > input[i-1]+input[i-2]+input[i-3]:
                part2 += 1 
    return part1, part2

if __name__== "__main__":
    part1 = part2 = 0
    r1, r2 = main(part1, part2)
    print("Result part1 : {} and part2 : {}".format(r1, r2))