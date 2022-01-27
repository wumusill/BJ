import sys

n = int(input())
for _ in range(n):
    h, w, n = map(int, sys.stdin.readline().split())
    if n % h != 0:
        back = str((n // h) + 1)
    else:
        back = str((n // h))
    if len(back) == 1:
        back = '0' + back
    floor = str(n % h)
    if floor == '0':
        floor = str(h)
    print(int(floor + back))