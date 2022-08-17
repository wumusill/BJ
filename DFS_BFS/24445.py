from collections import deque
import sys

n, m, r = map(int, sys.stdin.readline().split())
distance = [0] * (n + 1)
queue = deque([r])
distance[r] = 1

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(n + 1):
    graph[i].sort(reverse=True)

cnt = 1
while queue:
    x = queue.popleft()
    for i in graph[x]:
        if distance[i] == 0:
            cnt += 1
            distance[i] = cnt
            queue.append(i)


for answer in distance[1:]:
    print(answer)