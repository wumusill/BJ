import sys

n, k = map(int, sys.stdin.readline().split())
coins = list(int(sys.stdin.readline()) for _ in range(n))
dp = [int(1e9)] * (k + 1)

for i in range(1, k + 1):                               # 1원부터 k원까지 순회
    for coin in coins:                                  # 갖고 있는 동전 순회
        if i % coin == 0:                               # 한 종류의 동전으로 만들 수 있는 금액
            dp[i] = min(dp[i], i // coin)
        if i - coin > 0:
            dp[i] = min(dp[i], dp[i - coin] + 1)        # k원 만들 수 있는 동전 개수 = (k-coin)원 동전 개수 + 1개(coin)

# print(dp)
print(dp[k] if dp[k] != int(1e9) else -1)               # 못 만드는 금액은 -1 출력