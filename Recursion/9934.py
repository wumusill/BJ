import sys


# 재귀 함수
def recursion(num_list, n, k):
    # 중앙값 추가
    mid = (2 ** n - 1) // 2
    mat[k - n].append(num_list[mid])

    # 종료 조건 : 중앙값의 인덱스가 0이면 = 현재 탐색 중인 노드가 leaf
    if mid == 0:
        return
    # 리스트를 중앙값 기준으로 왼, 오른쪽 나누어 재귀
    return recursion(num_list[:mid], n - 1, k), recursion(num_list[mid+1:], n - 1, k)


k = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().strip().split()))
mat = [[] for _ in range(k)]
recursion(num_list, k, k)
for ans in mat:
    print(*ans)
############################################################################################
# 위 풀이와 같은 속도를 보이는 재귀를 사용하지 않는 풀이
K = int(input())
bn = list(map(int, input().split()))
graph = []

for i in range(K):
    A = bn[::2]
    graph.append(A)
    bn = bn[1::2]

for i in range(K - 1, -1, -1):
    print(*graph[i])