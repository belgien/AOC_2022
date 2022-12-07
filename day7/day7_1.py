## Day 7 - Part 1 

def readFile(filename):
    lines = open(filename,"r").readlines()
    result = []
    for line in lines:
        result.append(line.strip())
    return result

def solve(list):
    arr = []
    dict = {}
    for line in list:
        match line.split():
            case ["$", "cd", "/"]:
                arr.append("/")
                continue
            case ["$", "cd", x]:
                if x != "..":
                    arr.append(line.split()[2])
                else:
                    arr.pop()
            case ["$", "ls"]:
                continue
            case ["dir", x]:
                continue
            case [s, x]:
                temp = arr[:]
                for p in range(len(temp)):
                    f = "/".join(temp)
                    if f in dict:
                        dict.update({f: dict[f] + int(s)})
                        temp.pop()
                    else:
                        dict[f] = int(s)
                        temp.pop()
    total = [s for (f,s) in dict.items() if 100000 >= s]
    return sum(total)
            
if __name__ == "__main__":
    print("Total: " + str(solve(readFile("day7/day7_input"))))
