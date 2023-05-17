import sys
from collections import deque

n = int(sys.stdin.readline())
graph = [[] for _ in range(n + 1)]
visited = [0 for _ in range(n + 1)]

a, b = map(int, sys.stdin.readline().split())
m = int(sys.stdin.readline())
for _ in range(m):
    x, y = map(int, sys.stdin.readline().split())
    graph[x].append(y)
    graph[y].append(x)

q = deque()
q.append((a, 0))
visited[a] = 1
while q:
    x, res = q.popleft()
    if x == b:
        print(res)
        break
    for i in graph[x]:
        if visited[i] == 0:
            q.append((i, res + 1))
            visited[i] = 1
else:
    print(-1)