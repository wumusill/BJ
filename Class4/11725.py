from collections import deque
import sys


n = int(sys.stdin.readline())
graph = [[] for _ in range(n + 1)]
parent = [-1] * (n + 1)
parent[1] = 1

for _ in range(n - 1):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)

q = deque()
q.append(1)

while q:
    x = q.popleft()
    for i in graph[x]:
        if parent[i] == -1:
            parent[i] = x
            q.append(i)

for ans in parent[2:]:
    print(ans)