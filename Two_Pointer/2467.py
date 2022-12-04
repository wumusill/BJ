import sys

n = int(sys.stdin.readline())
num_l = list(map(int, sys.stdin.readline().split()))

f_idx = 0
b_idx = n - 1
nearest = float('inf')
res_left, res_right = 0, 0

while f_idx < b_idx:
    res = num_l[f_idx] + num_l[b_idx]
    if abs(res) < nearest:
        res_left, res_right = num_l[f_idx], num_l[b_idx]
        nearest = abs(res)

    if res < 0:
        f_idx += 1
    elif res > 0:
        b_idx -= 1
    else:
        break

print(res_left, res_right)