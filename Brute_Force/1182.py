import sys
from itertools import combinations


n, s = map(int, sys.stdin.readline().strip().split())
l = list(map(int, sys.stdin.readline().strip().split()))
ans = 0

# 입력 받은 리스트로 만들 수 있는 모든 조합
for i in range(1, n + 1):
    nCr = list(combinations(l, i))
    for case in nCr:
        if sum(case) == s:
            ans += 1

print(ans)
##################################################################
# dfs 활용한 다른 사람 풀이
# 240ms
n, s = map(int, input().split())
lst = list(map(int, input().split()))
answer = 0


def dfs(level, total):
    global answer

    if level == n:
        if total == s:
            answer += 1
        return

    dfs(level + 1, total + lst[level])
    dfs(level + 1, total)


dfs(0, 0)

if s == 0:
    print(answer - 1)
else:
    print(answer)