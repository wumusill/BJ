import sys
from collections import deque

queue = deque()

n, m, k, x = map(int, sys.stdin.readline().split())
array = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
distance = [0] * (n + 1)
ans = []

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    array[a].append(b)

for i in array[x]:
    queue.append(i)
    visited[i] = True
    distance[i] = 1

visited[x] = True

while queue:
    i = queue.popleft()
    for j in array[i]:
        if visited[j] == False:
            queue.append(j)
            visited[j] = True
            distance[j] = distance[i] + 1

for r in range(1, n + 1):
    if distance[r] == k:
        ans.append(r)

ans.sort()

if not ans:
    print(-1)
else:
    for b in ans:
        print(b)