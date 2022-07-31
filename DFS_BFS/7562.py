from collections import deque
import sys

n = int(sys.stdin.readline())
for _ in range(n):
    queue = deque()
    i = int(sys.stdin.readline())
    start_x, start_y = map(int, sys.stdin.readline().split())
    final_x, final_y = map(int, sys.stdin.readline().split())

    if start_x == final_x and start_y == final_y:
        print(0)
        continue

    visited = [[0] * i for _ in range(i)]
    distance = [[0] * i for _ in range(i)]

    visited[start_x][start_y] = 1
    queue.append((start_x, start_y))

    dx = [-2, -2, 2, 2, -1, 1, -1, 1]
    dy = [-1, 1, -1, 1, -2, -2, 2, 2]
    while queue:
        x, y = queue.popleft()
        breaker = False
        for k in range(8):
            nx = x + dx[k]
            ny = y + dy[k]
            if nx < 0 or ny < 0 or nx >= i or ny >= i:
                continue
            if visited[nx][ny] == 0:
                visited[nx][ny] = 1
                distance[nx][ny] = distance[x][y] + 1
                if nx == final_x and ny == final_y:
                    print(distance[final_x][final_y])
                    breaker = True
                    break
                else:
                    queue.append((nx, ny))
        if breaker:
            break