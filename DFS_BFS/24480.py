from collections import deque
import sys

n, m, r = map(int, sys.stdin.readline().split())
stack = deque()
graph = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)
cnt = 1

for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1, (n + 1)):
    graph[i].sort()

stack.append(r)

while stack:
    # 오름차순 stack을 pop하면 내림차순으로 방문하게 됨
    x = stack.pop()
    # stack에 한 노드가 여러 번 append 됐을 수 있으니 다시 방문 체크
    # 방문 순서를 기록하고 cnt += 1
    if visited[x] == 0:
        visited[x] = cnt
        cnt += 1
    for j in graph[x]:
        # 처음 방문한 노드라면 stack에 오름차순 append
        if visited[j] == 0:
            stack.append(j)

for answer in visited[1:]:
    print(answer)