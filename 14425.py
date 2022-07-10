import sys

n, m = map(int, sys.stdin.readline().split())
ans_dict = {}

for i in range(n):
    s = sys.stdin.readline()
    ans_dict[s] = 0

for j in range(m):
    new_s = sys.stdin.readline()
    if new_s in ans_dict.keys():
        ans_dict[new_s] += 1

print(sum(ans_dict.values()))