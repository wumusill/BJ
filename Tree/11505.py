import sys
from math import ceil, log2


def build_tree(t, numbers):
    tree_size = 2 ** (t + 1)
    tree = [1] * tree_size

    # 리프 노드에 입력 받은 수열 입력하는 반복문
    for index, number in enumerate(numbers):
        index += 2 ** t
        tree[index] = number

    # 입력 받은 리프 노드 데이터를 활용하여 부모 노드를 계산하는 반복문
    for index in range(2 ** t - 1, -1, -1):
        tree[index] = (tree[index * 2] * tree[index * 2 + 1]) % 1000000007

    return tree


def query(tree, start_index, end_index):
    result = 1

    while start_index <= end_index:
        if start_index % 2 == 1:
            result *= tree[start_index] % 1000000007
        if end_index % 2 == 0:
            result *= tree[end_index] % 1000000007

        start_index = (start_index + 1) // 2
        end_index = (end_index - 1) // 2

    print(int(result % 1000000007))


def update(tree, index, value):
    tree[index] = value
    index //= 2

    while index:
        tree[index] = (tree[index * 2] * tree[index * 2 + 1]) % 1000000007
        index //= 2


n, m, k = map(int, sys.stdin.readline().split())
nums = [int(sys.stdin.readline()) for _ in range(n)]
t = ceil(log2(n))
segment_tree = build_tree(t, nums)

for _ in range(m + k):
    command, a, b = map(int, sys.stdin.readline().split())
    if command == 1:
        update(segment_tree, a + (2 ** t - 1), b)
    elif command == 2:
        if a > b: a, b = b, a
        query(segment_tree, a + (2 ** t - 1), b + (2 ** t - 1))