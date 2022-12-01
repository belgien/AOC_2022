## Day 1 - Part 1

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

print(calories.pop())