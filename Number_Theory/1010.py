import sys
input = sys.stdin.readline

m = int(input())

for _ in range(m):
    res = 1
    n, r = map(int, input().split())
    for i in range(r, r-n,-1):
        res *= i
    print(res)