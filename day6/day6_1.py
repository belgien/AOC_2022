## Day 6 - Part 1 + 2

def readFile(filename):
    lines = open(filename,"r").readlines()
    return [*lines[0]]

def solve(lines, messageSize):
    for index in range(len(lines)):
        if index >= messageSize - 1:
            if len(set(lines[index-messageSize:index])) == messageSize:
                return index

if __name__ == "__main__":
    print("Part 1 total: " + str(solve(readFile("day6/day6_input.txt"), 4)))
    print("Part 2 total: " + str(solve(readFile("day6/day6_input.txt"), 14)))
