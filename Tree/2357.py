import sys
from math import log2


def solution(min_tree, max_tree, a, b, k):
    start_idx, end_idx = a + 2 ** k - 1, b + 2 ** k - 1
    mn, mx = min(min_tree[start_idx], min_tree[end_idx]), max(max_tree[start_idx], max_tree[end_idx])

    while start_idx <= end_idx:
        if start_idx % 2 == 1:
            mn = min(mn, min_tree[start_idx])
            mx = max(mx, max_tree[start_idx])
        if end_idx % 2 == 0:
            mn = min(mn, min_tree[end_idx])
            mx = max(mx, max_tree[end_idx])

        start_idx = (start_idx + 1) // 2
        end_idx = (end_idx - 1) // 2

    print(mn, mx)


n, m = map(int, sys.stdin.readline().split())
k = int(log2(n) + 1)
min_t = [int(1e9)] * ((2 ** k) * 2)
max_t = [0] * ((2 ** k) * 2)

# 리프 노드에 입력 받은 값 기록
for i in range(2 ** k, 2 ** k + n):
    num = int(sys.stdin.readline())
    min_t[i] = num
    max_t[i] = num

# 부모 노드의 값 갱신
for i in range(2 ** k - 1, -1, -1):
    min_t[i] = min(min_t[i * 2], min_t[i * 2 + 1])
    max_t[i] = max(max_t[i * 2], max_t[i * 2 + 1])

# 범위 입력 받아서 함수 실행
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    solution(min_t, max_t, a, b, k)


# 3 1
# 1
# 2
# 3
# 1 1