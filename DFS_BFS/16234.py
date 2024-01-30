import sys
from collections import deque


def bfs(a, b, visited):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    coord, q = [(a, b)], deque([(a, b)])                    # 인구 이동 국가와 queue에 자기 자신 기록
    res = nations[a][b]                                     # 인구 총합

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            diff = abs(nations[nx][ny] - nations[x][y])     # 인접 국가와 인구 차이 계산
            if visited[nx][ny] and L <= diff <= R:          # 방문이 가능한 국가 and 범위 내의 인구 차이
                q.append((nx, ny))
                visited[nx][ny] = False                     # 방문 처리
                res += nations[nx][ny]                      # 인구 총합 갱신
                coord.append((nx, ny))                      # 인구 이동 국가에 기록

    return coord, res, visited                              # 인구 이동 국가, 인구 총합, 방문 기록 반환


N, L, R = map(int, sys.stdin.readline().split())
nations = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

answer = 0
while True:
    unite = []                                              # 인구 이동이 발생할 국가들 기록할 리스트
    visited = [[True for _ in range(N)] for _ in range(N)]  # 모든 국가 방문 가능
    for a in range(N):                                      # 모든 국가 순회
        for b in range(N):
            if visited[a][b]:                               # 방문 가능한 국가라면 방문 처리하고 함수 실행
                visited[a][b] = False
                coord, res, visited = bfs(a, b, visited)

                if len(coord) > 1:                          # 인구 이동이 가능하다면 == 국가가 두 개 이상이면
                    unite.append([coord, res])              # 국가들의 좌표와 인구의 총합 기록

    if unite:                                               # 인구 이동 처리하는 조건문, 인구 이동이 발생할 국가들의 기록이 있으면
        answer += 1                                         # 인구 이동 발생 횟수 갱신
        for coord, res in unite:
            val = res // len(coord)                         # 인구 평균 계산
            for x, y in coord:                              # 국경 열린 국가들끼리 순회하며 인구 이동
                nations[x][y] = val
    else:                                                   # 인구 이동이 더 이상 발생하지 않으면 while문 종료
        break

print(answer)