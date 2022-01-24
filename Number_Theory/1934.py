import sys
input = sys.stdin.readline

def lcm(a, b):
    c, d = max(a, b), min(a, b)
    t = 1
    while t > 0:
        t = c % d
        c, d = d, t
    answer = int(a*b/c)

    return answer

n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    print(lcm(a, b))