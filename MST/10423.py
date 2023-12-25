import sys

n, m, k = map(int, sys.stdin.readline().split())
plants = list(map(int, sys.stdin.readline().split()))


def find(parent, x):
    if parent[x] == x:
        return x
    return find(parent, parent[x])


def union(parent, a, b):
    a, b = find(parent, a), find(parent, b)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a


# 발전소라면 부모를 0으로 설정, 나머진 자기 자신으로 설정
parent = [0] * (n + 1)
for i in range(1, n + 1):
    if i not in plants:
        parent[i] = i

lines = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]
lines.sort(key=lambda x:x[2])
answer = 0

for a, b, c in lines:
    a, b = find(parent, a), find(parent, b)
    if a != b:
        answer += c
        union(parent, a, b)

print(answer)