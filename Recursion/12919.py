import sys

s = list(sys.stdin.readline().strip())
t = list(sys.stdin.readline().strip())
ans = 0


def recursion(t):
    global ans
    if s == t:
        ans = 1
        return
    if len(t) == 0:
        return
    if t[-1] == "A":
        recursion(t[:-1])
    if t[0] == "B":
        recursion(t[::-1][:-1])


recursion(t)
print(ans)