import sys
from itertools import combinations


while True:
    n = list(map(int, sys.stdin.readline().split()))
    if n[0] == 0:
        break
    k = n[0]
    nums = n[1:]
    nC6 = combinations(nums, 6)
    for i in nC6:
        print(*i)
    print()