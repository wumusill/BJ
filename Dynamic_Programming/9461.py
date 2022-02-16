dp = [0] * 101
dp[0] = 1
dp[1] = 1
dp[2] = 1

for k in range(3, 101):
    dp[k] = dp[k-2] + dp[k-3]

t = int(input())

for _ in range(t):
    i = int(input())
    print(dp[i-1])