import sys


t = int(sys.stdin.readline())
for _ in range(t):
    n, r = map(int, sys.stdin.readline().strip().split())
    if r == 0:
        print(1)
        continue
    for i in range(n - 1, n - r, -1):
        n *= i
    for j in range(r - 1, r - r, -1):
        r *= j
    print(n // r % 1000000007)