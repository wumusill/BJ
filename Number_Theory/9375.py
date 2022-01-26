from math import factorial
import sys
input = sys.stdin.readline()

n = int(input)
c = int(input)
clothes = []
for _ in range(n):
    for _ in range(c):
        a, b = input.split()
        clothes.append(b)
