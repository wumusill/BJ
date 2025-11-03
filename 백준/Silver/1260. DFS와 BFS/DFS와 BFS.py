import sys
from collections import deque


def dfs(v, visited, answer):
    visited[v] = False
    answer.append(v)
        
    for next_node in graph[v]:
        if visited[next_node]:
            dfs(next_node, visited, answer)


def bfs(v):
    visited, answer = [True] * (n + 1), []
    visited[v] = False
    queue = deque([v])
    
    while queue:
        x = queue.popleft()
        answer.append(x)

        for next_node in graph[x]:
            if visited[next_node]:
                queue.append(next_node)
                visited[next_node] = False

    return answer


n, m, v = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, n + 1):
    graph[i].sort()

visited, answer = [True] * (n + 1), []
dfs(v, visited, answer)
print(*answer)
print(*bfs(v))