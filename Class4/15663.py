import sys
from itertools import permutations

n, m = map(int, sys.stdin.readline().split())
l = sorted(map(int, sys.stdin.readline().strip().split()))

ans = sorted(set(permutations(l, m)))

for i in ans:
    print(*i)