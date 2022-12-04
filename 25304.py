import sys

x = int(sys.stdin.readline())
n = int(sys.stdin.readline())

res = 0
for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    res += a * b

if res == x:
    print('Yes')
else:
    print('No')