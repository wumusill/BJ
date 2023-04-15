import sys

n = int(sys.stdin.readline())
l = list(map(int, sys.stdin.readline().split()))

dp = l.copy()

for i in range(n):
    a = l[i]
    for j in range(i, n):
        b = l[j]
        if a < b:
            dp[j] = max(dp[j], dp[i] + l[j])

print(max(dp))

####################################################################################

n = int(input())

sequence = list(map(int, input().split()))

dp_table = [0] * 1001

for j in range(n):
    num = sequence[j]
    # True == 1
    if dp_table[num]:
        dp_table[num] = max(max(dp_table[:num]) + num, dp_table[num])
    # False == 0
    # dp_table[num] == 0
    # 값을 인덱스로 하여 해당 인덱스에 나올 수 있는 가장 큰 수 저장
    else:
        dp_table[num] = max(dp_table[:num]) + num

print(max(dp_table))