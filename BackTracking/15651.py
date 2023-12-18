# itertools : 1604ms
from itertools import product

a, b = map(int, input().split())
arr = [i for i in range(1, a + 1)]
nPr = product(arr, repeat=b)

for j in nPr:
    print(' '.join(map(str, j)))
######################################################
# 백트래킹 : 1960ms
import sys

n, m = map(int, sys.stdin.readline().split())
case = []


def solution(l, m):
    if len(l) == m:
        print(*l)
        return

    for i in range(1, n + 1):
        case.append(i)
        solution(case, m)
        case.pop()


for i in range(1, n + 1):
    case.append(i)
    solution(case, m)
    case.pop()