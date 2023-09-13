from collections import deque
import sys

n = int(sys.stdin.readline())
q = deque(map(int, sys.stdin.readline().strip().split()))
ans = []

for i in range(n):
    q[i] = (i + 1, q[i])

while q:
    idx, cnt = q.popleft()
    ans.append(idx)
    if cnt > 0:
        q.rotate(-(cnt-1))
    else:
        q.rotate(-cnt)
    # print(q)

print(*ans)