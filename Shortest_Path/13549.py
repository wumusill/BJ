from collections import deque
import sys

n, k = map(int, sys.stdin.readline().rstrip().split())
visited = [-1] * 100001
visited[n] = 0

queue = deque()
queue.append((n, 0))

while queue:
    x, t = queue.popleft()

    if x == k:
        print(t)
        break

    l = [x * 2, x - 1, x + 1]
    for i in range(3):
        if 0 <= l[i] <= 100000:
            if i == 0 and visited[l[i]] == -1:
                visited[l[i]] = t
                queue.appendleft((l[i], t))
            elif i == 1 and visited[l[i]] == -1:
                visited[l[i]] = t + 1
                queue.append((l[i], t + 1))
            elif i == 2 and visited[l[i]] == -1:
                visited[l[i]] = t + 1
                queue.append((l[i], t + 1))