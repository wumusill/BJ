dp = [[0, 0] for _ in range(42)]
dp[0] = [1, 0]
dp[1] = [0, 1]

for i in range(2, 41):
    dp[i][0] = dp[i-1][0] + dp[i-2][0]
    dp[i][1] = dp[i-1][1] + dp[i-2][1]

t = int(input())
for _ in range(t):
    i = int(input())
    print(*dp[i])