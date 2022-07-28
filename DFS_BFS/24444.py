from collections import deque
import sys

n, m, r = map(int, sys.stdin.readline().split())
queue = deque()
visited = [0] * (n + 1)
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1, n + 1):
    graph[i].sort()

queue.append(r)
idx = 1
visited[r] = 1

while queue:
    x = queue.popleft()
    for i in graph[x]:
        if visited[i] == 0:
            idx += 1
            visited[i] = idx
            queue.append(i)

for answer in visited[1:]:
    print(answer)