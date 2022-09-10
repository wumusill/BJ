import sys
import heapq

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
graph = [[] for _ in range(n + 1)]


def solution(n, start, end):
    INF = int(1e9)
    visited = [INF] * (n + 1)
    # 큐 초기 설정, 출발지 세팅
    q = []
    heapq.heappush(q, (0, start))
    visited[start] = 0
    while q:
        # 가장 짧은 거리와 노드
        dist, now = heapq.heappop(q)
        # 이미 다른 최단 거리가 존재한다면 continue
        if visited[now] < dist:
            continue
        # 현재 그래프와 연결된 노드 순회
        for i in graph[now]:
            # 현재 노드에서 다음 노드로 필요한 비용 계산
            cost = dist + i[1]
            # 비용이 최솟값이라면, 기록하고 큐에 추가
            if cost < visited[i[0]]:
                visited[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    # 도착지까지 최단 거리 return
    return visited[end]


for _ in range(m):
    a, b, cost = map(int, sys.stdin.readline().split())
    # a에서 b로 갈 수 있는 필요한 cost
    graph[a].append((b, cost))

start, end = map(int, sys.stdin.readline().split())

print(solution(n, start, end))