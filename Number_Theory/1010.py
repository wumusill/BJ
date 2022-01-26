from math import factorial
import sys
input = sys.stdin.readline

m = int(input())

for _ in range(m):
    r, n = map(int, input().split())
    ans = factorial(n) // (factorial(r) * factorial(n - r))
    print(ans)