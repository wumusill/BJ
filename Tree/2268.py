import sys
from math import log2


def query(segment_tree, start_index, end_index):
    result = 0

    while start_index <= end_index:
        if start_index % 2 == 1:
            result += segment_tree[start_index]
        if end_index % 2 == 0:
            result += segment_tree[end_index]

        start_index = (start_index + 1) // 2
        end_index = (end_index - 1) // 2

    print(result)


def update(segment_tree, index, value):
    diff = value - segment_tree[index]
    segment_tree[index] = value
    index //= 2

    while index:
        segment_tree[index] += diff
        index //= 2


n, m = map(int, sys.stdin.readline().split())
k = int(log2(n) + 1)                                                    # 트리 사이즈 계산
tree = [0] * ((2 ** k) * 2)                                             # 트리 선언

for _ in range(m):
    command, b, c = map(int, sys.stdin.readline().split())

    if command == 0:
        if b > c:                                                       # b가 c보다 작다는 보장이 없음
            b, c = c, b                                                 # 만약 b가 더 크다면 swap
        start_idx, end_idx = b + (2 ** k - 1), c + (2 ** k - 1)
        query(tree, start_idx, end_idx)

    elif command == 1:
        idx = b + (2 ** k - 1)
        update(tree, idx, c)