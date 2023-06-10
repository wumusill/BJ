from collections import deque
import sys

n, k = map(int, sys.stdin.readline().strip().split())
q = deque([i for i in range(1, n + 1)])
ans_l = []
cnt = 0

while q:
    x = q.popleft()
    cnt += 1
    if cnt == k:
        ans_l.append(x)
        cnt = 0
    else:
        q.append(x)

ans = "<"
for element in ans_l:
    ans += str(element) + ", "
ans = ans[:-2]
ans += ">"
print(ans)