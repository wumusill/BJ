import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

# 단방향 그래프
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((b, c))

# 자기 자신 거리 0으로 갱신 & 경로 기록할 리스트 초기화
distance = [[int(1e9) for _ in range(n + 1)] for _ in range(n + 1)]
course = [[[i] for _ in range(n + 1)] for i in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == j:
            distance[i][j] = 0

# 인접 노드 거리와 경로 갱신
for a in range(1, n + 1):
    for b, c in graph[a]:
        distance[a][b] = min(distance[a][b], c)
        course[a][b] = [a, b]

# 플로이드 워셜로 최소 거리 갱신
# 거리가 갱신될 때마다 경로 갱신 : a -> k + k -> b 가 최소라면, (k -> b)의 k 제거해서  a -> k -> b 기록
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            if distance[a][b] > distance[a][k] + distance[k][b]:
                distance[a][b] = distance[a][k] + distance[k][b]
                course[a][b] = course[a][k] + course[k][b][1:]

# 거리가 초기 값이랑 같은 경우 == 갈 수 없는 노드 -> 0으로 거리 갱신
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if distance[i][j] == int(1e9):
            distance[i][j] = 0

# 결과물 출력
for i in range(1, n + 1):
    print(*distance[i][1:])

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if not course[i][j][1:]:
            print(0)
        else:
            res = [len(course[i][j])] + [i] + course[i][j][1:]
            print(*res)