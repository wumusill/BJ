import sys


def find_p(parent, x):
    if parent[x] == x:
        return x
    return find_p(parent, parent[x])


def union_p(parent, a, b):
    a = find_p(parent, a)
    b = find_p(parent, b)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a


t = int(sys.stdin.readline())

for _ in range(t):
    n, m = map(int, sys.stdin.readline().split())
    answer = 0

    parent = [0] * (n + 1)
    for i in range(1, n + 1):
        parent[i] = i

    for i in range(m):
        a, b = map(int, sys.stdin.readline().split())
        if find_p(parent, a) != find_p(parent, b):
            union_p(parent, a, b)
            answer += 1

    print(answer)