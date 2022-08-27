import sys

n, k = map(int, sys.stdin.readline().split())
l = sorted(map(int, sys.stdin.readline().split()), reverse=True)
print(l[k - 1])