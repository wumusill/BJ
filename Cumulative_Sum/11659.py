import sys

n, t = map(int, sys.stdin.readline().split())
l = list(map(int, sys.stdin.readline().split()))

sum_l = [0]
_sum = 0
for num in l:
    _sum += num
    sum_l.append(_sum)

for _ in range(t):
    start_idx, end_idx = map(int, sys.stdin.readline().split())
    print(sum_l[end_idx] - sum_l[start_idx - 1])


    # [0, 5, 9, 12, 14, 15]