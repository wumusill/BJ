# pypy3 944ms, python3 시간 초과
import sys

v, e = map(int, sys.stdin.readline().split())

# 그래프와 거리 초기화
graph = [[] for _ in range(v + 1)]
distance = [[int(1e9) for _ in range(v + 1)] for _ in range(v + 1)]

# 단방향 그래프
for _ in range(e):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((b, c))

# 자기 자신 거리 0으로 초기화
for a in range(1, v + 1):
    for b in range(1, v + 1):
        if a == b:
            distance[a][b] = 0

# 인접한 노드 거리 갱신
for a in range(1, v + 1):
    for b, c in graph[a]:
        distance[a][b] = c

# 플로이드 워셜 연산 : a에서 b로 가는 최단거리 갱신
for k in range(1, v + 1):
    for a in range(1, v + 1):
        for b in range(1, v + 1):
            distance[a][b] = min(distance[a][b], distance[a][k] + distance[k][b])

# 모든 노드를 순회
# a에서 b로 갔다가 다시 a로 돌아올 수 있는 최단 거리 계산
res = int(1e9)
for a in range(1, v + 1):
    for b in range(a + 1, v + 1):
        if a == b:
            continue
        res = min(res, distance[a][b] + distance[b][a])

# 만약 사이클이 발생하지 않으면 -1 출력
if res >= int(1e9):
    print(-1)
else:
    print(res)
#####################################################################################
# 다익스트라 알고리즘으로 구현
# 메모리 초과
import sys
import heapq

v, e = map(int, sys.stdin.readline().split())

# 그래프와 거리 초기화
graph = [[] for _ in range(v + 1)]
distance = [[int(1e9) for _ in range(v + 1)] for _ in range(v + 1)]

# 단방향 그래프
h = []
for _ in range(e):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((b, c))                                 # 그래프 갱신
    distance[a][b] = min(distance[a][b], c)                 # 거리 갱신
    heapq.heappush(h, (c, a, b))                     # 힙에 추가


while h:
    c, a, b = heapq.heappop(h)

    # 출발지와 도착지가 같다면 사이클 : 비용 기준 최소 힙이므로 가장 먼저 나온 사이클이 최솟값
    if a == b:
        print(c)
        break

    # 이미 기록된 거리가 더 작다면 패스
    if distance[a][b] < c:
        continue

    # b에서 갈 수 있는 노드 순회
    for new, temp_c in graph[b]:
        new_c = c + temp_c
        if new_c < distance[a][new]:
            distance[a][new] = new_c
            heapq.heappush(h, (new_c, a, new))

# 힙을 다 돌았다면 -1
else:
    print(-1)
#####################################################################################
import sys

v, e = map(int, sys.stdin.readline().split())


# 플로이드 워셜 연산 함수화 : a에서 b로 가는 최단거리 갱신
def floyd():
    for k in range(1, v + 1):
        for a in range(1, v + 1):
            for b in range(1, v + 1):
                # distance[a][b] = min(distance[a][b], distance[a][k] + distance[k][b]) 는 시간 초과
                # 조건문을 사용하니 패스
                if distance[a][b] > distance[a][k] + distance[k][b]:
                    distance[a][b] = distance[a][k] + distance[k][b]


# 그래프와 거리 초기화
graph = [[] for _ in range(v + 1)]
distance = [[int(1e9) for _ in range(v + 1)] for _ in range(v + 1)]

# 단방향 그래프
for _ in range(e):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((b, c))
    distance[a][b] = c

# 자기 자신 거리 0으로 초기화
for a in range(1, v + 1):
    distance[a][a] = 0

# 플로이드 워셜 연산 실행
floyd()

# 모든 노드를 순회
# a에서 b로 갔다가 다시 a로 돌아올 수 있는 최단 거리 계산
res = int(1e9)
for a in range(1, v + 1):
    for b in range(a + 1, v + 1):
        if a == b:
            continue
        # res = min(res, distance[a][k] + distance[k][b]) 는 시간 초과, 마찬가지로 조건문 사용
        if res > distance[a][b] + distance[b][a]:
            res = distance[a][b] + distance[b][a]

# 만약 사이클이 발생하지 않으면 -1 출력
if res >= int(1e9):
    print(-1)
else:
    print(res)