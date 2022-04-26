import sys

n, k = map(int, sys.stdin.readline().split())
l = list(map(int, sys.stdin.readline().split()))

num = sum(l[:k])
ans = num

for i in range((n - k)):
    num = num - l[i] + l[i + k]
    ans = max(num, ans)

print(ans)