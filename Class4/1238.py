import sys
import heapq

n, m, x = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((b, c))


def solution(start, end):
    INF = int(1e9)
    visited = [INF] * (n + 1)
    q = []
    heapq.heappush(q, (0, start))
    visited[start] = 0
    while q:
        cost, now = heapq.heappop(q)
        if cost > visited[now]:
            continue
        for i in graph[now]:
            if visited[i[0]] > cost + i[1]:
                visited[i[0]] = cost + i[1]
                heapq.heappush(q, (cost + i[1], i[0]))
    return visited[end]


# 모든 학생들이 거리 기록
distance = [0] * (n + 1)
for i in range(1, n + 1):
    distance[i] = solution(i, x) + solution(x, i)

print(max(distance))