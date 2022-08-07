import sys


n = int(sys.stdin.readline())
l = list(map(int, sys.stdin.readline().rstrip().split()))

# 증가하는 수열을 기록하기 위한 dp
dp = [1] * n

for i in range(n):
    for j in range(i):
        if l[i] > l[j]:
            dp[i] = max(dp[j] + 1, dp[i])

# 감소하는 수열을 기록하기 위한 dp
re_dp = [1] * n

for i in range(-1, -(n + 1), -1):
    for j in range(-1, i, -1):
        if l[i] > l[j]:
            re_dp[i] = max(re_dp[j] + 1, re_dp[i])

# 두 dp를 보면서 가장 긴 바이토닉 수열 길이 출력
answer = 0
for idx in range(n):
    answer = max(answer, dp[idx] + re_dp[idx] - 1)

print(answer)