import sys

n, m = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
ans = 0
stack = []

for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1, n + 1):
    if visited[i] == False:
        visited[i] = True
        stack.append(graph[i])
        ans += 1
    while stack:
        node = stack.pop()
        for i in node:
            if visited[i] == False:
                visited[i] = True
                stack.append(graph[i])

print(ans)