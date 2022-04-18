from collections import deque
import sys

queue = deque()
input = sys.stdin.readline()

n, m = map(int, input.split())

graph = [[] for _ in range(100001)]
visited = [False] * (100001)
queue.append((n, 0))
visited[n] = True

while queue:
    case = queue.popleft()
    node = case[0]
    time = case[1]
    dx = [node - 1, node + 1, node * 2]

    if node == m:
        print(time)
        break
    for x in dx:
        if 0 <= x and x <= 100000:
            graph[node].append(x)

    for i in graph[node]:
        if not visited[i]:
            queue.append((i, time + 1))
            visited[i] = True
################################################################################

n, m = map(int, input.split())

max_num = 100000
visited = [0] * (max_num + 1)


def bfs():
    q = deque()
    q.append(n)
    while q:
        x = q.popleft()
        if x == m:
            print(visited[x])
            break
        for j in (x - 1, x + 1, x * 2):
            if 0 <= j <= max_num and not visited[j]:
                visited[j] = visited[x] + 1
                q.append(j)


bfs()