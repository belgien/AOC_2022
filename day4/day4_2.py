## Day 4 - Part 2

def readFile(filename):
    lines = open(filename,"r").readlines()
    result = []
    for num in lines:
        result.append(num.strip())
    return result

def solve(list):
    counter = 0
    for item in list:
        range = item.split(",")
        x = range[0].split("-")
        y = range[1].split("-")
        if max(int(x[1]),int(y[1])) - min(int(x[0]),int(y[0])) <= int(x[1]) - int(x[0]) + int(y[1]) - int(y[0]):
            counter += 1
    return counter

if __name__ == "__main__":
    print("Total: " + str(solve(readFile("day4/day4_input"))))
