import sys
from math import gcd

n = int(sys.stdin.readline())
nums = list(int(sys.stdin.readline()) for _ in range(n))

# 연속된 원소들의 차
diff = [nums[i] - nums[i - 1] for i in range(1, n)]

# diff의 최대공배수 구하기
res = gcd(diff[0], diff[1])
for i in range(2, n - 1):
    res = gcd(res, diff[i])

answer = 0
for i in diff:
    if res > 0:
        answer += i // res - 1

print(answer)