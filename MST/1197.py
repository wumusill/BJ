import sys


def find(parent, x):
    if parent[x] == x:
        return x
    return find(parent, parent[x])


def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a


v, e = map(int, sys.stdin.readline().rstrip().split())
answer = 0

parent = [0] * (v + 1)
for i in range(1, v + 1):
    parent[i] = i

lines = []
for _ in range(e):
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    lines.append((a, b, c))

lines.sort(key=lambda x: x[2])

for line in lines:
    a = line[0]
    b = line[1]
    cost = line[2]
    if find(parent, a) != find(parent, b):
        union(parent, a, b)
        answer += cost

print(answer)