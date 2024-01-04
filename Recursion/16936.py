import sys

n = int(sys.stdin.readline())
l = list(map(int, sys.stdin.readline().split()))


def recursion(now):
    if len(now) == n:
        print(*now)
        return

    last = now[-1]
    new1 = last * 2
    new2 = last // 3
    if new1 in l:
        now.append(new1)
        recursion(now)
    if last % 3 == 0 and new2 in l:
        now.append(new2)
        recursion(now)


for num in l:
    recursion([num])