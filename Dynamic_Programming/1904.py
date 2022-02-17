import sys

dp = [0] * 1000000
dp[0] = 1
dp[1] = 2

for i in range(2, 1000000):
    dp[i] = (dp[i-1] + dp[i-2]) % 15746

n = int(sys.stdin.readline())

print(dp[n-1])