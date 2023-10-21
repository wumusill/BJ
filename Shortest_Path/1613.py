# 시간 초과
import sys

# 그래프 초기화
n, m = map(int, sys.stdin.readline().split())
graph = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

# 인접한 그래프 선후 관계 갱신
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a][b] = -1
    graph[b][a] = 1

# 플로이드 워셜로 선후 관계 갱신
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            if graph[a][k] == -1 and graph[k][b] == -1:
                graph[a][b] = -1
                graph[b][a] = 1

# 출력
s = int(sys.stdin.readline())
for _ in range(s):
    a, b = map(int, sys.stdin.readline().split())
    print(graph[a][b])
#####################################################################################
# 위 코드와 다른 점은 플로이드 워셜 구간을 함수화 하여 실행
import sys

n, m = map(int, sys.stdin.readline().split())
graph = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a][b] = -1
    graph[b][a] = 1


def floyd():
    for k in range(1, n + 1):
        for a in range(1, n + 1):
            for b in range(1, n + 1):
                if graph[a][k] == -1 and graph[k][b] == -1:
                    graph[a][b] = -1
                    graph[b][a] = 1


floyd()

s = int(sys.stdin.readline())
for _ in range(s):
    a, b = map(int, sys.stdin.readline().split())
    print(graph[a][b])