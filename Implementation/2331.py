# 51604 KB, 68ms
import sys

a, p = sys.stdin.readline().rstrip().split()
p = int(p)
num = {i:0 for i in range(1, 240000)}
num[int(a)] = 1

while True:
    res = 0
    for i in a:
        res += int(i) ** p

    if num[res] == 0:
        num[res] = num[int(a)] + 1
        a = str(res)
    else:
        print(num[res] - 1)
        break
################################################################
# 31120 KB, 40ms
import sys

a, p = map(int, sys.stdin.readline().split())
seq = [a]

while True:
    next_num = sum([int(i) ** p for i in str(seq[-1])])
    if next_num in seq:
        print(seq.index(next_num))
        break
    else:
        seq.append(next_num)