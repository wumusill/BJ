import sys

n = int(sys.stdin.readline())
a = sorted(map(int, sys.stdin.readline().split()))
b = sorted(map(int, sys.stdin.readline().split()), reverse=True)
ans = 0
for x, y in zip(a, b):
    ans += x * y

print(ans)