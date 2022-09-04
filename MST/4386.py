import sys

n = int(sys.stdin.readline())
parent = [i for i in range(n)]
stars = []
costs = []
answer = 0


def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]


def union(x, y):
    x = find(x)
    y = find(y)
    if x < y:
        parent[y] = x
    else:
        parent[x] = y


for j in range(n):
    star = list(map(float, sys.stdin.readline().split()))
    stars.append(star)

# 모든 별과 별 사이의 비용을 계산
for a in range(n):
    for b in range(n):
        cost = round(((stars[a][0] - stars[b][0]) ** 2 + (stars[a][1] - stars[b][1]) ** 2) ** 0.5, 2)
        # a와 b 사이의 cost
        costs.append((a, b, cost))

# 비용 순으로 정렬
costs.sort(key=lambda x: x[2])

# 부모가 다르다면 union, 비용 합산
while costs:
    a, b, cost = costs.pop(0)
    if find(a) != find(b):
        union(a, b)
        answer += cost

# print(stars)
# print(costs)
print(round(answer, 2))


# 3
# 2.0 4.0
# 1.0 1.0
# 2.0 2.0
# 3.41

# 6
# 4 1
# 5 8
# 2 1
# 8 4
# 2 9
# 1 4
# 18.32