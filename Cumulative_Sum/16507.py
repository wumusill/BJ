# 시간초과
import sys


def solution(mat, x1, y1, x2, y2):
    area = (y2 - y1 + 1) * (x2 - x1 + 1)
    res = 0

    for i in range(x1 - 1, x2):
        for j in range(y1 - 1, y2):
            res += mat[i][j]

    avg = res // area
    return avg


r, c, q = map(int, sys.stdin.readline().split())
mat = []
for _ in range(r):
    l = list(map(int, sys.stdin.readline().split()))
    mat.append(l)

for _ in range(q):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    print(solution(mat, x1, y1, x2, y2))
###############################################################################
# 정답
import sys

r, c, q = map(int, sys.stdin.readline().split())

# matrix prefix sum 기록할 dp 초기화
dp = [[0 for _ in range(c + 1)] for _ in range(r + 1)]

# matrix prefix sum 계산 & 기록
for i in range(1, r + 1):
    arr = list(map(int, sys.stdin.readline().split()))
    for j in range(1, c + 1):
        dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1] + arr[j-1]

for i in range(q):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    area = (x2 - x1 + 1) * (y2 - y1 + 1)
    res = dp[x2][y2] - dp[x1 - 1][y2] - dp[x2][y1 - 1] + dp[x1 - 1][y1 - 1]
    print(res // area)