import sys

l = sorted([int(sys.stdin.readline()) for _ in range(5)])
print(int(sum(l) / 5))
print(l[2])