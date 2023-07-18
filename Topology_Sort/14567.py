import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n + 1)]
indegree = [0] * (n + 1)
ans = [0] * (n + 1)
q = deque()

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    indegree[b] += 1

# 필요한 학기 수
semester = 1
for i in range(1, n + 1):
    if indegree[i] == 0:
        # 학기 수를 같이 큐에 삽입
        q.append((i, semester))

while q:
    x, semester = q.popleft()
    # 학기 수 기록
    ans[x] = semester
    for i in graph[x]:
        indegree[i] -= 1
        if indegree[i] == 0:
            # 진입 차수가 새로이 0이 된 과목에 대해 학기 + 1
            q.append((i, semester + 1))

print(*ans[1:])