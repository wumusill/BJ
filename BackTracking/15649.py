# 순열
import itertools

N, M = map(int, input().split())
arr = [i for i in range(1, N + 1)]

nPr = itertools.permutations(arr, M)
for _ in nPr:
    print(' '.join(map(str, _)))
######################################################
# 백트래킹
import sys

n, m = map(int, sys.stdin.readline().split())
case = []


def solution(m, case):
    if len(case) == m:
        print(*case)
        return

    for i in range(1, n + 1):
        if i not in case:
            case.append(i)
            solution(m, case)
            case.pop()


for i in range(1, n + 1):
    solution(m, [i])