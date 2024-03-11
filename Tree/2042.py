import sys
from math import ceil, log2


def build_tree(numbers, t):
    tree_size = 2 ** (t + 1)
    tree = [0] * tree_size

    for idx, num in enumerate(numbers):                         # 수열 리프 노드에 입력
        tree[idx + 2 ** t] = num

    for i in range(2 ** t - 1, -1, -1):                         # 부모 노드 연산
        tree[i] = tree[i * 2] + tree[i * 2 + 1]

    return tree


def update(tree, index, value):
    diff = value - tree[index]
    tree[index] = value
    index //= 2

    while index:
        tree[index] += diff
        index //= 2


def query(tree, start_index, end_index):
    result = 0

    while start_index <= end_index:
        if start_index % 2 == 1:
            result += tree[start_index]
        if end_index % 2 == 0:
            result += tree[end_index]

        start_index = (start_index + 1) // 2
        end_index = (end_index - 1) // 2

    print(result)


n, m, k = map(int, sys.stdin.readline().split())
nums = [int(sys.stdin.readline()) for _ in range(n)]
t = ceil(log2(n))
segment_tree = build_tree(nums, t)

for _ in range(m + k):
    command, a, b = map(int, sys.stdin.readline().split())
    if command == 1:
        update(segment_tree, a + (2 ** t - 1), b)
    elif command == 2:
        query(segment_tree, a + (2 ** t - 1), b + (2 ** t - 1))