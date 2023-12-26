# itertools : 176ms
import sys
from itertools import permutations

n, m = map(int, sys.stdin.readline().split())
l = sorted(map(int, sys.stdin.readline().split()))

case = permutations(l, m)
for i in case:
    print(*i)
######################################################
# 백트래킹 : 216ms
import sys

n, m = map(int, sys.stdin.readline().split())
l = sorted(map(int, sys.stdin.readline().split()))


def solution(m, case):
    if len(case) == m:
        print(*case)
        return

    for element in l:
        if element not in case:
            case.append(element)
            solution(m, case)
            case.pop()

case = []
for i in l:
    case.append(i)
    solution(m, case)
    case.pop()