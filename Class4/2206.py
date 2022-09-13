'''
CPython은 지역변수에 접근하는 시간이 더 짧기 때문에 함수 내부에서 좀 더 빠르게 실행, 첫번째 풀이 코드 전체를 함수로 감싸면 아마 시간초과가 안 나옴
https://stackoverflow.com/questions/11241523/why-does-python-code-run-faster-in-a-function
'''
# 함수 호출 -> 통과 ##############################################################
from collections import deque
import sys

n, m = map(int, sys.stdin.readline().split())
visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
mat = [list(map(int, list(sys.stdin.readline().rstrip()))) for _ in range(n)]
q = deque()

# visited[0][0][0]에는 벽을 안부순 경우
# visited[0][0][1]에는 벽을 부순 경우
visited[0][0][0] = 1
q.append((0, 0, 0))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs():
    while q:
        x, y, w = q.popleft()
        # 먼저 도착하는 값이 출력되기에 최솟값이 보장
        if x == n - 1 and y == m - 1:
            return visited[x][y][w]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 맵 범위 안이라면
            if 0 <= nx < n and 0 <= ny < m:
                # 다음 위치로 이동할 수 있고, 방문하지 않았다면
                if mat[nx][ny] == 0 and visited[nx][ny][w] == 0:
                    visited[nx][ny][w] = visited[x][y][w] + 1
                    q.append((nx, ny, w))
                # 다음 위치가 벽이고, 벽을 아직 부수지 않았다면
                elif mat[nx][ny] == 1 and w == 0:
                    visited[nx][ny][1] = visited[x][y][w] + 1
                    q.append((nx, ny, 1))
    return -1


print(bfs())
#############################################################################
# 함수 호출 X -> 시간 초과 ######################################################
from collections import deque
import sys

n, m = map(int, sys.stdin.readline().split())
visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
mat = [list(map(int, list(sys.stdin.readline().rstrip()))) for _ in range(n)]
q = deque()

# visited[0][0][0]에는 벽을 안부순 경우
# visited[0][0][1]에는 벽을 부순 경우
visited[0][0][0] = 1
q.append((0, 0, 0))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
while q:
    x, y, w = q.popleft()
    # 먼저 도착하는 값이 출력되기에 최솟값이 보장
    if x == n - 1 and y == m - 1:
        print(visited[x][y][w])
        break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 맵 범위 안이라면
        if 0 <= nx < n and 0 <= ny < m:
            # 다음 위치로 이동할 수 있고, 방문하지 않았다면
            if mat[nx][ny] == 0 and visited[nx][ny][w] == 0:
                visited[nx][ny][w] = visited[x][y][w] + 1
                q.append((nx, ny, w))
            # 다음 위치가 벽이고, 벽을 아직 부수지 않았다면
            elif mat[nx][ny] == 1 and w == 0:
                visited[nx][ny][1] = visited[x][y][w] + 1
                q.append((nx, ny, 1))
else:
    print(-1)


# 6 4
# 0000
# 1110
# 1000
# 0000
# 0111
# 0000
# 9


# 7 6
# 000000
# 111110
# 001110
# 010000
# 011111
# 011111
# 000000
# 12