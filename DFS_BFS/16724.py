# 47020 KB, 3236 ms
# 다른 풀이와 비교해봤을 때 메모리는 낮은 편이지만 시간은 높은 편
# 모든 노드를 방문할 때 까지 dfs 수행하고, 한 번 dfs 수행할 때마다 safe zone 설치
# 지금 탐색 중인 노드가 dfs 중간 지점일 수 있으므로 주변 노드가 현재 노드로 향하는지도 확인
import sys

n, m = map(int, sys.stdin.readline().split())
matrix = [list(sys.stdin.readline().rstrip()) for _ in range(n)]
visited = [[True for _ in range(m)] for _ in range(n)]
move = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
answer = 0

for a in range(n):
    for b in range(m):
        if visited[a][b]:                                         # 현재 노드 방문한 적 없으면 safe zone 설치 후 dfs 수행
            answer += 1
            visited[a][b] = False
            stack = [(a, b, matrix[a][b])]
            while stack:
                x, y, command = stack.pop()
                move_x, move_y = move[command]
                nx, ny = x + move_x, y + move_y
                if visited[nx][ny]:
                    stack.append((nx, ny, matrix[nx][ny]))
                    visited[nx][ny] = False

                for i in range(4):                                # 현재 노드가 하나의 dfs 중 중간 노드일 수 있므로 사방위 순회
                    nx, ny = x + dx[i], y + dy[i]

                    if nx < 0 or ny < 0 or nx >= n or ny >= m:
                        continue

                    new_command = matrix[nx][ny]                  # 만약 사방에 위치한 노드의 이동 경로가 현재 노드라면
                    move_x, move_y = move[new_command]            # 그 노드도 현재 dfs에 포함되어야 함 -> 방문 처리, stack 추가
                    if visited[nx][ny] and nx + move_x == x and ny + move_y == y:
                        stack.append((nx, ny, new_command))
                        visited[nx][ny] = False

print(answer)
#######################################################################################################################
# 어차피 bfs가 활용된다면 dfs 없이 bfs로만 구현 가능하지 않을까
# 막상 해보니 stack을 q로 바꾸는거 말고는 로직이 바뀌지 않아 코드도 거의 그대로
# 약간의 메모리 증가와 약간의 시간 감소 : 48108 KB, 3088 ms
from collections import deque
import sys

n, m = map(int, sys.stdin.readline().split())
matrix = [list(sys.stdin.readline().rstrip()) for _ in range(n)]
visited = [[True for _ in range(m)] for _ in range(n)]
move = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
answer = 0

for a in range(n):
    for b in range(m):
        if visited[a][b]:
            answer += 1
            visited[a][b] = False
            q = deque([(a, b, matrix[a][b])])
            while q:
                x, y, command = q.popleft()
                move_x, move_y = move[command]
                nx, ny = x + move_x, y + move_y
                if visited[nx][ny]:
                    q.append((nx, ny, matrix[nx][ny]))
                    visited[nx][ny] = False

                for i in range(4):
                    nx, ny = x + dx[i], y + dy[i]

                    if nx < 0 or ny < 0 or nx >= n or ny >= m:
                        continue

                    new_command = matrix[nx][ny]
                    move_x, move_y = move[new_command]
                    if visited[nx][ny] and nx + move_x == x and ny + move_y == y:
                        q.append((nx, ny, new_command))
                        visited[nx][ny] = False

print(answer)

# 10 10
# DRDRRRRRRD
# RDRUDUUUUL
# URLDLRRRRD
# RRRRLRDLUD
# DDRLLDULUU
# DRULLLRDUU
# DULLDDDURU
# URLDDDDUUL
# DLRLRDUULL
# RRULRUUURU
# 12