import sys

n, m = map(int, sys.stdin.readline().split())
dic = {}

for _ in range(n):
    name = sys.stdin.readline()
    if name in dic.keys():
        dic[name] += 1
    else:
        dic[name] = 1

for _ in range(m):
    name = sys.stdin.readline()
    if name in dic.keys():
        dic[name] += 1
    else:
        dic[name] = 1

ans = 0
ans_l = []

for name, cnt in dic.items():
    if cnt == 2:
        ans += 1
        ans_l.append(name.strip('\n'))

ans_l.sort()
print(ans)
for i in ans_l:
    print(i)