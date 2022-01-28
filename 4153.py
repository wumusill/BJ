import sys

while True:
    tri = list(map(int, sys.stdin.readline().split()))
    if sum(tri) == 0:
        break
    c = max(tri)
    tri.remove(c)
    ans = 0
    for i in tri:
        ans = ans + i ** 2
    if c ** 2 == ans:
        print('right')
    else:
        print('wrong')