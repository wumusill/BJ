import sys

n, m = map(int, sys.stdin.readline().strip().split())
l = sorted(map(int, sys.stdin.readline().strip().split()))

for i in l:
    if i <= m:
        m += 1

print(m)