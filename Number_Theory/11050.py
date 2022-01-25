import sys
from itertools import combinations
input = sys.stdin.readline

n, k = map(int, input().split())

l = [1 for _ in range(n)]

nCr = combinations(l, k)
print(len(list(nCr)))