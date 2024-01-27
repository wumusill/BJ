import sys
import heapq

n, m, k = map(int, sys.stdin.readline().split())

# 그래프 설정
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((b, c))

# 힙에 (거리, 출발 노드) 추가
h = [(0, 1)]
distance = [[int(1e9)] * k for _ in range(n + 1)]               # 1에서 n번 노드까지의 최단 거리 k개만 기록할 행렬
distance[1][0] = 0                                              # 출발 노드 거리 설정
while h:
    now_dist, now = heapq.heappop(h)                            # 현재 최소 거리와 노드
    if distance[now][k - 1] < now_dist:                         # k 번째 거리가 현재 최소 거리보다 크면 아무 일 없음
        continue

    for next, next_dist in graph[now]:                          # 인접 노드 순회
        if distance[next][k - 1] <= now_dist + next_dist:       # 다음 노드로 가는 k 번째 거리가 더 작으면 아무 일 없음
            continue
        distance[next][k - 1] = now_dist + next_dist            # 다음 노드로 가는 거리 계산
        distance[next].sort()                                   # 다음 노드로 가는 k개의 거리 오름차순 정렬
        heapq.heappush(h, (now_dist + next_dist, next))   # 힙에 다음 노드와 가는 거리 추가

for city in range(1, n + 1):
    print(distance[city][k - 1] if distance[city][k - 1] != int(1e9) else -1)