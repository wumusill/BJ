import sys

n = int(sys.stdin.readline())
l = list(map(int, sys.stdin.readline().split()))

dp = l.copy()

for i in range(n):
    a = l[i]
    for j in range(i, n):
        b = l[j]
        if a < b:
            dp[j] = max(dp[j], dp[i] + l[j])

print(max(dp))