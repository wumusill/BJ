num_com = int(input())
n = int(input())
graph = [[] * n for _ in range(num_com + 1)]

for _ in range(n):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

result = 0
visited = [False] * (num_com + 1)

def dfs(start):
    visited[start] = True
    for i in graph[start]:
        if visited[i] == False:
            global result
            result += 1
            dfs(i)

dfs(1)

print(result)