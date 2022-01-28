import sys

a, b, v = map(int, sys.stdin.readline().split())

v -= a

one_day = a - b
days = v // one_day
remainder = v % one_day
ans = 0

if days == 0 and v != 0:
    ans += 1
else:
    if remainder == 0:
        ans += days
    else:
        ans += days + 1

ans += 1

print(ans)