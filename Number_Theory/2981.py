from math import gcd
import sys
input = sys.stdin.readline

n = int(input())
num_list = [int(input()) for _ in range(n)]
diff_list = []

for i in range(1, n):
    diff_list.append(num_list[i] - num_list[i-1])

_gcd = diff_list[0]
for i in range(1, len(diff_list)):
    _gcd = gcd(_gcd, diff_list[i])

answer_list = []

for i in range(2, int(_gcd ** 0.5)+1):
    if _gcd % i == 0:
        answer_list.append(i)
        answer_list.append(_gcd // i)

answer_list.append(_gcd)
answer_list = list(set(answer_list))
answer_list.sort()

print(*answer_list)