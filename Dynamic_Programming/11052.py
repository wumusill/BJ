import sys


n = int(sys.stdin.readline())
l = [0] + list(map(int, sys.stdin.readline().strip().split()))
dp = [0 for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, i + 1):
        dp[i] = max(dp[i], dp[i - j] + l[j])

print(dp[n])