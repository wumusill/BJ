import sys

# 부모를 찾아주는 함수
def find(parent, x):
    if parent[x] == x:
        return x
    return find(parent, parent[x])


def union(parent, a, b):
    a = find(parent, a)         # 부모를 찾음
    b = find(parent, b)
    if a > b:                   # 작은 노드를 부모로 삼음
        parent[a] = b
    else:
        parent[b] = a


n = int(sys.stdin.readline())   # 노드 개수
m = int(sys.stdin.readline())   # 간선 개수

parent = [i for i in range(n + 1)]      # 자기 자신을 부모로 설정

# 간선 정보 저장
lines = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]

# 간선들 비용순 오름차순 정렬
lines.sort(key=lambda x: x[2])

# 간선 순회
answer = 0
for a, b, c in lines:
    if find(parent, a) != find(parent, b):      # 부모가 다르다면
        union(parent, a, b)                     # 노드를 연결하고 부모 갱신
        answer += c                             # 비용 갱신

print(answer)