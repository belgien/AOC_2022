## Day 5 - Part 2

c1 = ['Q', 'W', 'P', 'S', 'Z', 'R', 'H', 'D']
c2 = ['V', 'B', 'R', 'W', 'Q', 'H', 'F']
c3 = ['C', 'V', 'S', 'H']
c4 = ['H', 'F', 'G']
c5 = ['P', 'G', 'J', 'B', 'Z']
c6 = ['Q', 'T', 'J', 'H', 'W', 'F', 'L']
c7 = ['Z', 'T', 'W', 'D', 'L', 'V', 'J', 'N']
c8 = ['D', 'T', 'Z', 'C', 'J', 'G', 'H', 'F']
c9 = ['W', 'P', 'V', 'M', 'B', 'H']
stacks = [c1, c2, c3, c4, c5, c6, c7, c8, c9]

def readFile(filename):
    lines = open(filename,"r").readlines()
    result = []
    for index, x in enumerate(lines):
        if index > 9:
            result.append(x.strip())
    return result

def solve(list, stack):
    temp = ''
    arr = []
    for move in list:
        temp = ''.join(c for c in move if (c.isdigit() or c ==' '))
        arr.append(temp.split())

    temp2 = []
    for x in arr:
        f = int(x[1]) - 1
        t = int(x[2]) - 1
        for y in range(int(x[0])):
            temp2.append(stack[f].pop())
        temp2.reverse()
        stack[t] += temp2
        temp2 = []
    
    for column in stack:
        temp2.append(column.pop())
    return temp2

print(solve(readFile("day5/day5_input.txt"), stacks))
