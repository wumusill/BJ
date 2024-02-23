import sys


def floyd():
    for i in range(n):                              # 자기 자신 거리 0으로 갱신하는 반복문
        for j in range(n):
            if i == j:
                result[i][j] = 0

    for k in range(n):                              # 플로이드 워셜 알고리즘으로 최소 거리 갱신
        for a in range(n):
            for b in range(n):
                result[a][b] = min(result[a][b], distance[a][k] + distance[k][b])


def dfs(now, visited, depth, value):
    global answer

    if value > answer:                              # 현재 계산 거리가 정답보다 크면 더 계산할 필요 없음
        return

    if depth == n:                                  # 모든 노드를 순회했다면 최소 거리 갱신하고 재귀 종료
        answer = min(answer, value)
        return

    for next in range(n):                           # 노드 순회
        if visited[next]:                           # 방문 가능한 노드에 대하여 백트래킹
            visited[next] = False
            dfs(next, visited, depth + 1, value + result[now][next])
            visited[next] = True


n, depart = map(int, sys.stdin.readline().split())
distance = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
result = [[int(1e9) for _ in range(n)] for _ in range(n)]
visited, answer = [True] * n, float('inf')

# 두 함수 실행
floyd()
dfs(depart, visited, 0, 0)

print(answer)