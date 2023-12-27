# python3 : 시간 초과
# pypy3 : 7660ms
import sys

r, c = map(int, sys.stdin.readline().split())
mat = [list(sys.stdin.readline().rstrip()) for _ in range(r)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

visited = {letter: True for letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'}
visited[mat[0][0]] = False
answer = 1


def recursion(x, y, visited, dist):
    global answer
    answer = max(answer, dist)

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if nx < 0 or ny < 0 or nx >= r or ny >= c:
            continue

        alphabet = mat[nx][ny]
        if visited[alphabet]:
            visited[alphabet] = False
            recursion(nx, ny, visited, dist + 1)
            visited[alphabet] = True


recursion(0, 0, visited, 1)

print(answer)
######################################################################################
# python3 : 1232ms
# 집합을 활용하여 구현
import sys


def dfs(x, y):
    global mat, r, c
    answer = 0
    q = set()
    q.add((x, y, mat[x][y]))

    while q:
        x, y, visited = q.pop()
        answer = max(answer, len(visited))

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < r and 0 <= ny < c and mat[nx][ny] not in visited:
                q.add((nx, ny, visited + mat[nx][ny]))

    return answer


r, c = map(int, sys.stdin.readline().split())
mat = [list(sys.stdin.readline().rstrip()) for _ in range(r)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

print(dfs(0, 0))