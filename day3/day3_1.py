## Day 3 - Part 1

def readFile(filename):
    lines = open(filename,"r").readlines()
    result = []
    for num in lines:
        result.append(num.strip())
    return result

# Finds matching characters
def findMatchingChar(list):
    result = []
    for bag in list:
        result.append(set([*bag[0:len(bag)//2]]).intersection(set([*bag[len(bag)//2:len(bag)]])).pop())
    return result

# Finds value of matching characters
def findValue(list):
    total = 0
    for char in list:
        total += ord(char) - 96 if char.islower() else ord(char) - 38
    return total

if __name__ == "__main__":
    print("Total: " + str(findValue(findMatchingChar(readFile("day3\day3_input.txt")))))
