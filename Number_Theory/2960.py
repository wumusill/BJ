import sys


n, k = map(int, sys.stdin.readline().split())


def solution(n, k):
    l = [True] * (n + 1)
    l[0] = False
    l[1] = False

    cnt = 0
    for i in range(2, n + 1):
        if l[i]:
            for j in range(i, n + 1, i):
                if l[j]:
                    l[j] = False
                    cnt += 1
                if cnt == k:
                    return j


print(solution(n, k))