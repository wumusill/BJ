import sys

n, m = map(int, sys.stdin.readline().split())
parent = [i for i in range(n + 1)]
gods = [()]
costs = []


def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]


def union(a, b):
    a = find(a)
    b = find(b)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a


def cost(x1, x2, y1, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5


for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    gods.append((x, y))

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    if find(a) != find(b):
        union(a, b)

for i in range(1, n):
    for j in range(i + 1, n + 1):
        _cost = cost(gods[i][0], gods[j][0], gods[i][1], gods[j][1])
        costs.append((i, j, _cost))

costs.sort(key=lambda x: x[2])

answer = 0
for a, b, _cost in costs:
    if find(a) != find(b):
        union(a, b)
        answer += _cost

# 4.0도 4.00으로 출력되게 하는 format
print(format(answer, ".2f"))