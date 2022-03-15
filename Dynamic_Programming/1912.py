import sys

n = int(sys.stdin.readline())

dp = [0] * n
l = list(map(int, sys.stdin.readline().split()))

dp[0] = l[0]
for i in range(1, n):
    dp[i] = max(l[i], dp[i - 1] + l[i])

print(max(dp))