import sys


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


while True:
    n, m = map(int, sys.stdin.readline().split())
    if n == 0 and m == 0:
        break
    lines = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]
    lines.sort(key=lambda x: x[2])
    parent = [i for i in range(n)]
    answer = 0
    for a, b, c in lines:
        a, b = find(parent, a), find(parent, b)
        if a != b:
            union(parent, a, b)
        else:
            answer += c

    print(answer)