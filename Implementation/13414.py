import sys

k, l = map(int, sys.stdin.readline().split())

ID = []
cnt = {}
for _ in range(l):
    key = sys.stdin.readline().rstrip()
    ID.append(key)
    if key in cnt.keys():
        cnt[key] += 1
    else:
        cnt[key] = 1

answer = []
for i in ID:
    if len(answer) == k:
        break
    if cnt[i] == 1:
        answer.append(i)
    else:
        cnt[i] -= 1

for ans in answer:
    print(ans)