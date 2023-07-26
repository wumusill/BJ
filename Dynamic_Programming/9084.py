import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    coins = list(map(int, sys.stdin.readline().strip().split()))
    m = int(sys.stdin.readline())

    # m원까지 만들 수 있는 횟수 기록할 dp
    dp = [0] * (m + 1)
    dp[0] = 1

    # 갖고 있는 동전들 순회
    for coin in coins:
        # 순회 중인 동전부터 만들 수 있는 갯수 갱신
        for i in range(coin, m + 1):
            # ex) 2원을 가지고 있다면 0원을 만들 수 있는 횟수만큼 2원을 만들 수 있음
            dp[i] += dp[i - coin]
    print(dp[m])