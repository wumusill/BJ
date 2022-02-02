import sys
from itertools import combinations
from math import factorial

n, r = map(int, sys.stdin.readline().split())
ans = 1

for i in range(n, n-r, -1):
    ans *= i

print(ans // factorial(r))