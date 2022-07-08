import sys

a, b = map(int, sys.stdin.readline().split())
cnt = 1

while True:
    if b < a:
        print(-1)
        break
    if b == a:
        print(cnt)
        break
    if b % 10 == 1:
        b //= 10
    elif b % 2 == 0:
        b //= 2
    else:
        print(-1)
        break
    cnt += 1