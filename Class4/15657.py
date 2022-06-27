import sys
from itertools import combinations_with_replacement

n, m = map(int, sys.stdin.readline().split())
l = sorted(map(int, sys.stdin.readline().split()))

case = combinations_with_replacement(l, m)
for ans in case:
    print(*ans)