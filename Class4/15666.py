from itertools import combinations_with_replacement
import sys


n, m = map(int, sys.stdin.readline().split())
s = sorted(set(map(int, sys.stdin.readline().split())))
comb = sorted(combinations_with_replacement(s, m), key=lambda x: x[0])

for answer in comb:
    print(*answer)