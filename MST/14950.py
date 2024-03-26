import sys


def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]


def union(parent, a, b):
    a, b = find(parent, a), find(parent, b)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a


n, m, t = map(int, sys.stdin.readline().split())
parent = [i for i in range(n + 1)]
roads = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]
roads.sort(key=lambda x: x[2])
answer, cnt = 0, 0

for a, b, c in roads:
    a, b = find(parent, a), find(parent, b)
    if a != b:
        union(parent, a, b)
        answer += c                             # 간선 연결 비용
        answer += t * cnt                       # 간선 경계 비용
        cnt += 1                                # 연결된 간선 개수 갱신

print(answer)