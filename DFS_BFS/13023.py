import sys


n, m = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n)]
visited = [False] * n
ans = False

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)


def dfs(node, depth):
    global ans
    visited[node] = True
    if depth == 4:
        ans = True
        return
    for i in graph[node]:
        if not visited[i]:
            dfs(i, depth + 1)
    # 탐색에 실패했을 때 다시 False로 방문 취소
    visited[node] = False


for i in range(n):
    dfs(i, 0)
    if ans:
        break

if ans:
    print(1)
else:
    print(0)
##############################################################################################
# 탐색에 실패한 노드에 대해 방문 취소 설정을 하지 않아 틀림
# 함수로 구현하지 않고 스택으로 구현했을 때 방문 취소하는 방법??
# 그 방법을 못찾아서 틀린 코드
import sys


n, m = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n)]

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(n):
    visited = [False] * n
    stack = []
    stack.append((i, 0))
    flag = False
    while stack:
        x, y = stack.pop()
        visited[x] = True
        if y == 4:
            print(1)
            flag = True
            break
        for j in graph[x]:
            if visited[j] == False:
                stack.append((j, y+1))
    if flag:
        break
else:
    print(0)