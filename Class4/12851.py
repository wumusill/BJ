from collections import deque
import sys

queue = deque()

n, k = map(int, sys.stdin.readline().split())
visited = [[-1, 0] for _ in range(100001)]

queue.append(n)
visited[n][0] = 0
visited[n][1] = 1

while queue:
    second = queue.popleft()

    for i in [second + 1, second - 1, second * 2]:
        if 0 <= i <= 100000:
            if visited[i][0] == -1:
                visited[i][0] = visited[second][0] + 1
                visited[i][1] += visited[second][1]
                queue.append(i)
            elif visited[i][0] == visited[second][0] + 1:
                visited[i][1] += visited[second][1]

print(visited[k][0])
print(visited[k][1])