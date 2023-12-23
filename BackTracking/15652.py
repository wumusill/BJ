# itertools : 72ms
from itertools import combinations_with_replacement

n, t = map(int, input().split())
arr = [i for i in range(1, n + 1)]

nCr = combinations_with_replacement(arr, t)

for j in nCr:
    print(' '.join(map(str, j)))
######################################################
# 백트래킹 : 72ms
import sys

n, m = map(int, sys.stdin.readline().split())


def solution(m, case):
    if len(case) == m:
        print(*case)
        return

    for i in range(case[-1], n + 1):
        case.append(i)
        solution(m, case)
        case.pop()


for i in range(1, n + 1):
    solution(m, [i])