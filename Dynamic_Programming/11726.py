import sys

dp = [0] * 1001
dp[0] = 0
dp[1] = 1
dp[2] = 2

for i in range(3, 1001):
    dp[i] = dp[i - 2] + dp[i - 1]

n = int(sys.stdin.readline())
print(dp[n] % 10007)