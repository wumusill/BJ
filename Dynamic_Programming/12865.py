import sys

n, k = map(int, sys.stdin.readline().split())
items = []

for _ in range(n):
    w, v = map(int, sys.stdin.readline().split())
    items.append((w, v))

dp = [0] * 100001

for item in items:
    w, v = item
    # 무게 k부터 w까지 dp 탐색
    # dp에 기록된 무게와 만들 수 있는 무게 중 최대값 기록
    for i in range(k, w - 1, -1):
        dp[i] = max(dp[i], dp[i - w] + v)

print(dp[k])