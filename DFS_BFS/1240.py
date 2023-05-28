import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n + 1)]

# 그래프 정보 저장
# a 번째 리스트에는 b로 가는 거리가 튜플 형태로 저장
for _ in range(n - 1):
    a, b, dist = map(int, sys.stdin.readline().split())
    graph[a].append((b, dist))
    graph[b].append((a, dist))


# a와 b의 거리를 구해주는 bfs 함수
def bfs(a, b):
    visited = [-1] * (n + 1)
    q = deque()
    q.append((a, 0))
    visited[a] = 0
    while q:
        a, d = q.popleft()
        for y, dist in graph[a]:
            if visited[y] == -1:
                visited[y] = d + dist
                q.append((y, d + dist))

    return visited[b]


for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    print(bfs(a, b))