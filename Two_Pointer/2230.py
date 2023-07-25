import sys

n, m = map(int, sys.stdin.readline().split())
l = sorted(int(sys.stdin.readline()) for _ in range(n))
left, right = 0, 1
ans = l[-1] - l[0]

while right < n and left < n:
    res = l[right] - l[left]
    if res >= m:
        ans = min(res, ans)
        left += 1
    else:
        right += 1

print(ans)


# 7 4
# 1
# 8
# 15
# 16
# 17
# 18
# 22
# 4