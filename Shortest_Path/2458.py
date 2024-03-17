# 본인보다 키가 작거나 큰 인원이 (n - 1)명이라면 자신의 키 순서를 알 수 있음
# pypy3 : 113,300 KB, 1,344ms
import sys

n, m = map(int, sys.stdin.readline().split())
height = [[False for _ in range(n + 1)] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    height[a][b] = True                                 # height[a][b] = True : a는 b보다 키가 작음

for k in range(1, n + 1):                               # 플로이드 워셜 알고리즘 수행
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            if height[a][k] and height[k][b]:           # a가 k보다 작고, k가 b보다 작다면 a는 b보다 작음
                height[a][b] = True

answer = 0
for a in range(1, n + 1):
    know = 0
    for b in range(1, n + 1):
        know += height[a][b] + height[b][a]             # 본인보다 키가 작거나 키가 큰 인원 합계 계산
    if know == n - 1:                                   # 합계가 본인을 제외한 n - 1 이라면, 키 순서를 알 수 있음
        answer += 1                                     # 키 순서 알 수 있는 인원 갱신

print(answer)
#######################################################################################################################
# python3 : 35,380 KB, 872ms
import sys


def dfs(graph, node):                               # dfs를 수행하여 자식 노드의 개수 반환
    visited = [False] * (n + 1)
    stack = [node]
    result = 0

    while stack:
        now = stack.pop()
        for next in graph[now]:
            if not visited[next]:
                stack.append(next)
                visited[next] = True
                result += 1

    return result


n, m = map(int, sys.stdin.readline().split())
asc = [[] for _ in range(n + 1)]                    # 키 오름차순 그래프 a가 b보다 작음 -> graph[a].append(b)
desc = [[] for _ in range(n + 1)]                   # 키 내림차순 그래프 a가 b보다 작음 -> graph[b].append(a)

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    asc[a].append(b)
    desc[b].append(a)

answer = 0
for start in range(1, n + 1):
    res_asc = dfs(asc, start)                       # 키가 start보다 큰 사람의 수 계산
    res_desc = dfs(desc, start)                     # 키가 start보다 작은 사람의 수 계산

    if res_asc + res_desc == n - 1:                 # 계산된 두 값의 합이 자기 자신을 제외한 (n - 1)과 같다면 본인의 키 순서 파악 가능
        answer += 1

print(answer)