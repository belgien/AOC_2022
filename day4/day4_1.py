## Day 4 - Part 1

def readFile(filename):
    lines = open(filename,"r").readlines()
    result = []
    for num in lines:
        result.append(num.strip())
    return result

# Split list into subarrays, and check whether the range is within the other
def solve(list):
    counter = 0
    for item in list:
        range = item.split(",")
        x = range[0].split("-")
        y = range[1].split("-")
        if int(x[0]) >= int(y[0]) and int(x[1]) <= int(y[1]) or int(x[0]) <= int(y[0]) and int(x[1]) >= int(y[1]):
            counter += 1
    return counter

if __name__ == "__main__":
    print("Total: " + str(solve(readFile("day4/day4_input"))))
