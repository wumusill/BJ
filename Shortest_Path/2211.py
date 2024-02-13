import sys
import heapq

# 양방향 그래프 간선 정보 저장
v, e = map(int, sys.stdin.readline().split())
computers = [[] for _ in range(v + 1)]
for _ in range(e):
    a, b, c = map(int, sys.stdin.readline().split())
    computers[a].append((b, c))
    computers[b].append((a, c))

# 정답과 거리 초기화 및 갱신
answer = [0] * (v + 1)
distance = [float('inf')] * (v + 1)
distance[1] = 0

# 출발 노드 설정
h = []
heapq.heappush(h, (0, 1))

while h:
    cost, now = heapq.heappop(h)
    if cost > distance[now]:
        continue

    for next, c in computers[now]:
        new_distance = cost + c
        if distance[next] > new_distance:               # 새로운 방문 가능 최소 거리 등장
            distance[next] = new_distance               # 최소 거리 갱신
            heapq.heappush(h, (new_distance, next))     # 힙에 추가
            answer[next] = now                          # 최소 거리로 도달 직전 노드 기록

print(v - 1)
for idx, node in enumerate(answer):
    if idx > 1:
        print(idx, node)