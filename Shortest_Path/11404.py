import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
graph = [[] for _ in range(n + 1)]
ans = [[int(1e9) for _ in range(n + 1)] for _ in range(n + 1)]

# 단방향 그래프
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((b, c))

# 자기 자신 거리 0으로 갱신
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == j:
            ans[i][j] = 0

# 인접한 노드 거리 갱신
for a in range(1, n + 1):
    for b, c in graph[a]:
        ans[a][b] = min(ans[a][b], c)

# 플로이드 워셜로 최소 거리 갱신
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            ans[a][b] = min(ans[a][b], ans[a][k] + ans[k][b])

# (거리 == INF) = 갈 수 없는 노드는 거리 0으로 갱신하고 출력
for answer in ans[1:]:
    for x in range(1, n + 1):
        if answer[x] == int(1e9):
            answer[x] = 0
    print(*answer[1:])