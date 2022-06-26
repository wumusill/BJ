import sys
from itertools import permutations

n, m = map(int, sys.stdin.readline().split())
l = sorted(map(int, sys.stdin.readline().split()))

case = permutations(l, m)
for i in case:
    print(*i)