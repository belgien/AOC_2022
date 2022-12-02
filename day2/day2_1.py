## Day 2 - Part 1

def readFile(filename):
    with open(filename,"r") as f:
        lines = f.readlines()
    
    result = []
    for num in lines:
        result.append(num.split())
    return result

def solve(list):
    totalscore = 0
    for item in list:
        ## Opponent's move
        if item[0]=="A":
            player2 = 1
        elif item[0]=="B":
            player2 = 2
        elif item[0]=="C":
            player2 = 3

        ## Player's move
        if item[1]=="X":
            player1 = 1
        elif item[1]=="Y":
            player1 = 2
        elif item[1]=="Z":
            player1 = 3
        
        if player1 == player2 + 1 or player1 + 2 == player2:
            totalscore += 6
        elif player1 == player2:
            totalscore += 3
        totalscore += player1
    return totalscore

if __name__ == "__main__":
    print("Total score: " + str(solve(readFile("day2_input"))))
