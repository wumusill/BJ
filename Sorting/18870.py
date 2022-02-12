import sys

n = int(sys.stdin.readline())

l = list(map(int, sys.stdin.readline().split()))

sorted_set = sorted(set(l))
dict = {}

for i in range(len(sorted_set)):
    dict[sorted_set[i]] = i

for i in l:
    print(dict[i], end=' ')