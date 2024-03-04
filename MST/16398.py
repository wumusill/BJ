import sys


def find(parent, a):
    if parent[a] != a:
        parent[a] = find(parent, parent[a])
    return parent[a]


def union(parent, a, b):
    a, b = find(parent, a), find(parent, b)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a


n = int(sys.stdin.readline())
mat = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
parent = [i for i in range(n + 1)]

lines = []
for i in range(n):
    for j in range(i + 1, n):
        lines.append((i, j, mat[i][j]))

lines.sort(key=lambda x: x[2])

answer = 0
for a, b, c in lines:
    if find(parent, a) != find(parent, b):
        union(parent, a, b)
        answer += c

print(answer)