import sys
from itertools import combinations
from collections import deque

mat = [list(sys.stdin.readline().rstrip()) for _ in range(5)]
c = combinations([i for i in range(25)], 7)
potential = []
answer = 0

for sample in c:
    cnt = {'S': 0, 'Y': 0}
    for element in sample:
        x, y = element // 5, element % 5
        cnt[mat[x][y]] += 1
        if cnt['Y'] == 4:
            break
    else:
        potential.append(sample)


def bfs(q, sample, visited):
    global answer
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    v = 0

    while q:
        num = q.popleft()
        x, y = num // 5, num % 5
        v += 1
        if v == 7:
            answer += 1
            break

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or ny < 0 or nx > 4 or ny > 4:
                continue
            if (nx * 5 + ny) in sample and visited[nx][ny]:
                visited[nx][ny] = False
                q.append((nx * 5 + ny))


for sample in potential:
    q = deque([])
    visited = [[True for _ in range(5)] for _ in range(5)]
    q.append(sample[0])
    visited[sample[0] // 5][sample[0] % 5] = False
    bfs(q, sample, visited)

print(answer)