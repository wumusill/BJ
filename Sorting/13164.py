import sys


n, k = map(int, sys.stdin.readline().split())
l = list(map(int, sys.stdin.readline().split()))
diff_l = []

for i in range(1, n):
    diff_l.append(l[i] - l[i-1])

diff_l.sort(reverse=True)
print(sum(diff_l[k-1:]))


# 6 3
# 1 2 4 6 7 10
# 4