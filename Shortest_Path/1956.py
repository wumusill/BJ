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
    for b in range(1, v + 1):
        if a == b:
            continue
        res = min(res, distance[a][b] + distance[b][a])

# 만약 사이클이 발생하지 않으면 -1 출력
if res >= int(1e9):
    print(-1)
else:
    print(res)