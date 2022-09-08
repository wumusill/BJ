import sys

n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
dp = [1] * n

for i in range(n):
    for j in range(i):
        if nums[i] < nums[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))

#############################################################################
def solution(n, nums):
    dp = [1] * n

    for i in range(n):
        for j in range(i):
            if nums[i] < nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)


print(solution(n, nums))