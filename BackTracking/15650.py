# itertools 조합 활용 : 80ms
import itertools

N, M = map(int, input().split())
arr = [i for i in range(1, N + 1)]

nCr = itertools.combinations(arr, M)
for _ in nCr:
    print(' '.join(map(str, _)))
######################################################
# 백트래킹 활용 : 40ms
import sys

n, m = map(int, sys.stdin.readline().split())
case = []


def solution(m, case):
    if len(case) == m:
        print(*case)
        return
    for i in range(case[-1] + 1, n + 1):
        case.append(i)
        solution(m, case)
        case.pop()


for i in range(1, n + 1):
    case.append(i)
    solution(m, case)
    case.pop()