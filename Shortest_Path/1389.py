import sys

n, m = map(int, sys.stdin.readline().split())

# 거리 무한으로 초기화
INF = int(1e9)
dist = [[INF for _ in range(n + 1)] for _ in range(n + 1)]

# 양방향 그래프
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

# 자기 자신 거리 0으로 갱신
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            dist[a][b] = 0

# 인접한 노드 거리 갱신
for a in range(1, n + 1):
    for b in graph[a]:
        dist[a][b] = 1

# 플로이드 워셜 알고리즘으로 모든 노드에서 모든 노드까지 최소 거리 갱신
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            dist[a][b] = min(dist[a][b], dist[a][k] + dist[k][b])

# 케빈 베이컨의 수 계산
ans = [0] * (n + 1)
for i in range(1, n + 1):
    kevin = sum(dist[i][1:])
    ans[i] = kevin

# 케빈 베이컨의 수가 가장 작은 index 출력
# 가장 작은 베이컨의 수를 가진 index가 여러 개라면 가장 작은 index 하나만 출력
for i in range(1, n + 1):
    if ans[i] == min(ans[1:]):
        print(i)
        break