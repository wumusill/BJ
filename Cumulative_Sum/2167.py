import sys


n, m = map(int, sys.stdin.readline().strip().split())

# 2차원 배열 누적합을 기록할 dp
dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

# 누적합 기록하는 반복문
for i in range(1, n + 1):
    arr = list(map(int, sys.stdin.readline().strip().split()))
    for j in range(1, m + 1):
        dp[i][j] = dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1] + arr[j - 1]

# k번 입력 받아 누적합 계산
k = int(sys.stdin.readline())
for _ in range(k):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().strip().split())
    print(dp[x2][y2] - dp[x1- 1][y2] - dp[x2][y1 - 1] + dp[x1 - 1][y1 - 1])