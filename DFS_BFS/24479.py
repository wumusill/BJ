from collections import deque
import sys

n, m, r = map(int, sys.stdin.readline().rstrip().split())
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
answer = [0] * (n + 1)

for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(n + 1):
    graph[i].sort(reverse=True)

stack = deque()
stack.append(r)
ans = 1

while stack:
    node = stack.pop()
    visited[node] = True
    if answer[node] == 0:
        answer[node] = ans
        ans += 1

    for next_node in graph[node]:
        if not visited[next_node]:
            stack.append(next_node)


for i in range(1, (n + 1)):
    print(answer[i])