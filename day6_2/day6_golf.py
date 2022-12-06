## Day 6 - Part 1 + 2 Shortest Python Solution

l=open("day6_2/x").read()
f=lambda m:[i for i in range(len(l))if len(set(l[i:i+m]))==m][0]+m
print(f(4),f(14))