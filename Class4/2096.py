import sys

n = int(sys.stdin.readline())
max_mat = []
min_mat = []

l = list(map(int, sys.stdin.readline().split()))

max_l = list(l)
min_l = list(l)

for i in range(1, n):
    next_l = list(map(int, sys.stdin.readline().split()))
    max_dp = list(next_l)
    min_dp = list(next_l)
    for j in range(3):
        if j == 0:
            max_dp[j] += max(max_l[j], max_l[j + 1])
            min_dp[j] += min(min_l[j], min_l[j + 1])
        elif j == 1:
            max_dp[j] += max(max_l[j - 1], max_l[j], max_l[j + 1])
            min_dp[j] += min(min_l[j - 1], min_l[j], min_l[j + 1])
        else:
            max_dp[j] += max(max_l[j - 1], max_l[j])
            min_dp[j] += min(min_l[j - 1], min_l[j])

    max_l = list(max_dp)
    min_l = list(min_dp)

_max = max(max_l)
_min = min(min_l)

print(_max, _min)