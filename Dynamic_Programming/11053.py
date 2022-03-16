import sys

n = int(sys.stdin.readline())
l = list(map(int, sys.stdin.readline().split()))
dp = [1] * n


for i in range(n):
    for j in range(i):
        if l[i] > l[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))


# 1. 현재 위치(i)보다 이전에 있는 원소(j)가 작은지 확인
# 2. 작다면, 현재 위치의 이전 숫자 중, dp 최댓값을 구하고 그 길이에 1을 더해준다