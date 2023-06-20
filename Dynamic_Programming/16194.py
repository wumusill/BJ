import sys

n = int(sys.stdin.readline())
l = [0] + list(map(int, sys.stdin.readline().strip().split()))
dp = [10001] * (n + 1)
dp[0] = l[0]

# i개를 사기 위해 현재 기록된 값이 최솟값인지 or j개를 사고 i-j개를 사는 것이 최솟값인지 탐색
for i in range(1, n + 1):
    for j in range(1, i + 1):
        dp[i] = min(dp[i], l[j] + dp[i - j])

print(dp[n])