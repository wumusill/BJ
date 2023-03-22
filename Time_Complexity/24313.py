import sys

a, b = map(int, sys.stdin.readline().split())
c = int(sys.stdin.readline())
n = int(sys.stdin.readline())

for i in range(n, 101):
    res1 = a * i + b
    res2 = c * i
    if res1 > res2:
        print(0)
        break
else:
    print(1)
