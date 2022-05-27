import sys

n = int(sys.stdin.readline())
l = list(map(int, sys.stdin.readline().split()))
l.sort()

ans = l[(n - 1) // 2]

print(ans)