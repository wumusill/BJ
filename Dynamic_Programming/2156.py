import sys

t = int(sys.stdin.readline())
l = [int(sys.stdin.readline()) for _ in range(t)]

dp = [0] * t

dp[0] = l[0]
if t > 1:
    dp[1] = l[0] + l[1]

if t > 2:
    dp[2] = max(l[2] + l[1], l[2] + l[0], dp[1])

for i in range(3, t):
    dp[i] = max(dp[i-1], l[i] + dp[i-2], l[i] + l[i-1] + dp[i-3])

print(max(dp))