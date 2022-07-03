import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
deq = deque([i for i in range(1, n + 1)])

# 앞쪽에 가까울 경우 index만큼 왼쪽 회전
# 뒤쪽에 가까울 경위 len - index 만큼 오른쪽 회전

l = list(map(int, sys.stdin.readline().split()))
ans = 0

for num in l:
    idx = deq.index(num)
    if idx <= (len(deq) // 2):
        ans += idx
        for _ in range(idx):
            front = deq.popleft()
            deq.append(front)
    else:
        ans += (len(deq) - idx)
        for _ in range(len(deq) - idx):
            back = deq.pop()
            deq.appendleft(back)
    deq.popleft()

print(ans)