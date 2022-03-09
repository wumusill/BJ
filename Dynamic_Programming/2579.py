n = int(input())

dp = [0] * (n + 1)
stair = [0] + [int(input()) for _ in range(n)]

if n == 1:
    print(stair[1])
elif n == 2:
    print(sum(stair))
else:
    dp[1] = stair[1]
    dp[2] = dp[1] + stair[2]

    if n == 2:
        print(dp[2])

    for i in range(3, n + 1):
        dp[i] = max(dp[i - 3] + stair[i - 1], dp[i - 2]) + stair[i]

    print(dp[-1])