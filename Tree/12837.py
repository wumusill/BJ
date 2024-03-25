import sys
from math import ceil, log2


def build_tree(k):
    tree_size = 2 ** (k + 1)
    tree = [0] * tree_size
    return tree


def update(tree, index, value):
    tree[index] += value
    index //= 2
    while index:
        tree[index] += value
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


n, q = map(int, sys.stdin.readline().split())
k = ceil(log2(n))
segment_tree = build_tree(k)

for _ in range(q):
    a, b, c = map(int, sys.stdin.readline().split())
    if a == 1:
        update(segment_tree, b + 2 ** k - 1, c)
    elif a == 2:
        query(segment_tree, b + 2 ** k - 1, c + 2 ** k - 1)