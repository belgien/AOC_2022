## Day 1 - Part 2

f = open("day1_input","r")
lines = f.readlines()

result = []

for num in lines:
    result.append(num.strip())

calories = []
temp = 0

for num in result:
    if (num!=""):
        temp = temp + int(num)
    else:
        calories.append(temp)
        temp = 0

calories.sort()
calories.reverse()

total = 0

for x in range(3):
    total = total + calories[x]

print(total)