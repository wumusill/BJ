import sys
from math import sqrt

t = int(sys.stdin.readline())
for _ in range(t):

    x_1, y_1, r_1, x_2, y_2, r_2 = map(int, sys.stdin.readline().split())

    if x_1 == x_2 and y_1 == y_2 and r_1 == r_2:
        print(-1)
        continue

    d = sqrt((x_2 - x_1) ** 2 + (y_2 - y_1) ** 2)

    sum_of_radius = r_1 + r_2
    if r_1 >= r_2:
        differ_of_radius = r_1 - r_2
    else:
        differ_of_radius = r_2 - r_1

    if sum_of_radius < d or differ_of_radius > d:
        ans = 0
    elif sum_of_radius == d or differ_of_radius == d:
        ans = 1
    elif differ_of_radius < d < sum_of_radius:
        ans = 2

    print(ans)