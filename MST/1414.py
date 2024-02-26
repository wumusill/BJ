import sys


def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]


def union(a, b):
    a, b = find(a), find(b)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a


n = int(sys.stdin.readline())
computer = [list(sys.stdin.readline().rstrip()) for _ in range(n)]
cost = {val: idx for idx, val in enumerate('0abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')}
parent, answer = [i for i in range(n)], 0

line = []
for i in range(n):
    for j in range(n):
        c = cost[computer[i][j]]            # 랜선 비용
        line.append((i, j, c))              # (출발지, 도착지, 비용) 기록
        answer += c                         # 모든 랜선 비용

line.sort(key=lambda x: x[2])               # 랜선 비용 기준 오름차순 정렬

for a, b, c in line:                        # 랜선 순회
    if not c:                               # 비용이 0이면 넘어가기
        continue
    if find(a) != find(b):                  # 부모가 다르다면 연결 처리하고
        union(a, b)
        answer -= c                         # 랜선 연결 비용 차감

for i in range(n):                          # 마을 순회
    if find(i):                             # 부모가 0이 아니라면 모든 마을이 연결되지 않은 것
        print(-1)
        break
else:
    print(answer)