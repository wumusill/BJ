import sys

n, m = map(int, sys.stdin.readline().split())
l = sorted(map(int, sys.stdin.readline().split()))


def solution(m, case):
    if len(case) == m:
        print(*case)
        return

    for element in l:
        if element > case[-1]:
            case.append(element)
            solution(m, case)
            case.pop()

case = []
for i in l:
    case.append(i)
    solution(m, case)
    case.pop()