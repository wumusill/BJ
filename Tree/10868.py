import sys
from math import log2


def solution(tree, a, b, k):
    start_idx, end_idx = a + 2 ** k - 1, b + 2 ** k - 1
    result = min(tree[start_idx], tree[end_idx])

    while start_idx <= end_idx:
        if start_idx % 2 == 1:
            result = min(result, tree[start_idx])
        if end_idx % 2 == 0:
            result = min(result, tree[end_idx])

        start_idx = (start_idx + 1) // 2
        end_idx = (end_idx - 1) // 2

    print(result)


n, m = map(int, sys.stdin.readline().split())
k = int(log2(n) + 1)
segment = [int(1e9)] * (2 ** (k + 1))

# 입력 받은 데이터 리프 노드로 입력
for i in range(n):
    idx = i + (2 ** k)
    segment[idx] = int(sys.stdin.readline())

# 부모 노드 값 갱신
for i in range(2 ** k - 1, -1, -1):
    segment[i] = min(segment[i * 2], segment[i * 2 + 1])

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())

    # 계속 틀렸던 이유 : 두 수가 주어질 때 항상 오름차순이라는 보장이 없음
    # 내림차순으로 주어졌을 경우 swap
    if a > b:
        a, b = b, a

    solution(segment, a, b, k)