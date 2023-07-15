import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
q = deque()
ans = []

# 진입 차수와 그래프
indegree = [0] * (n + 1)
graph = [[] for _ in range(n + 1)]

# 진입 차수와 그래프 기록
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    indegree[b] += 1

# 진입 차수가 0인 것 큐에 삽입
for i in range(1, n + 1):
    if indegree[i] == 0:
        q.append(i)

# 연산 수행
while q:
    x = q.popleft()
    ans.append(x)
    for i in graph[x]:
        indegree[i] -= 1
        if indegree[i] == 0:
            q.append(i)

print(*ans)