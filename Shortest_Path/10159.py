import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
graph = [[False for _ in range(n + 1)] for _ in range(n + 1)]     # graph[a][b] = True -> a와 b 비교 결과를 알 수 있음을 의미

for i in range(1, n + 1):                                         # 자기 자신은 비교 가능
    graph[i][i] = True

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())                 # 입력 받은 비교 결과 기록
    graph[a][b] = True

for k in range(1, n + 1):                                         # 알고리즘 수행
    for a in range(1, n + 1):                                     # a > k, k > b 라면 a > b
        for b in range(1, n + 1):
            if graph[a][k] and graph[k][b]:
                graph[a][b] = True

for a in range(1, n + 1):                                         # 1번 노드부터 n번 노드까지 순회
    answer = 0
    for b in range(1, n + 1):
        if not graph[a][b] and not graph[b][a]:                   # (a, b), (b, a) 비교 결과를 알 수 없는 노드 개수 계산
            answer += 1

    print(answer)