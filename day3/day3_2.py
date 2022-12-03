## Day 3 - Part 2

def readFile(filename):
    lines = open(filename,"r").readlines()
    result = []
    for num in lines:
        result.append(num.strip())
    return result

# Splits list into groups of 3
def chunks(xs, n):
    n = max(1, n)
    return [xs[i:i+n] for i in range(0, len(xs), n)]

# Finds matching characters
def findMatchingChar(list):
    result = []
    for group in list:
        result.append(set([*group[0]]).intersection(set([*group[1]])).intersection(set([*group[2]])).pop())
    return result

# Finds value of matching characters
def findValue(list):
    total = 0
    for char in list:
        total += ord(char) - 96 if char.islower() else ord(char) - 38
    return total

if __name__ == "__main__":
    print("Total: " + str(findValue(findMatchingChar(chunks(readFile("day3\day3_input.txt"),3)))))
