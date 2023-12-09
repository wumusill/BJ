import sys
import heapq

n, m = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((b, c))
    graph[b].append((a, c))


def solution(start, end):
    # start 부터 모든 노드까지의 거리 기록
    visited = [int(1e9)] * (n + 1)

    # 출발 노드 초기화
    h = []
    heapq.heappush(h, (0, start))
    visited[start] = 0

    # 경로 계산
    while h:
        dist, now = heapq.heappop(h)

        # 이미 더 짧은 경로가 기록되어 있다면 pass
        if visited[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < visited[i[0]]:
                visited[i[0]] = cost
                heapq.heappush(h, (cost, i[0]))

    return visited[end]


print(solution(1, n))