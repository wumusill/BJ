import sys

n = int(sys.stdin.readline())
l = list(map(int, sys.stdin.readline().split()))
t, p = map(int, sys.stdin.readline().split())

ans_t = 0
for i in l:
    d, m = divmod(i, t)
    if m != 0:
        d += 1
    ans_t += d

ans_p1, ans_p2 = divmod(n, p)

print(ans_t)
print(ans_p1, ans_p2)