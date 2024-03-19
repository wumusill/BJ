# 구간 곱의 부호가 중요
# 양수는 1, 0, 음수는 -1로 통일하여 계산
import sys
from math import ceil, log2


def build_tree(nums, k):
    tree_size = 2 ** (k + 1)
    tree = [0] * tree_size

    for idx, val in enumerate(nums):
        idx += 2 ** k
        if val > 0:
            tree[idx] = 1
        elif val == 0:
            tree[idx] = 0
        else:
            tree[idx] = -1

    for i in range(2 ** k - 1, -1, -1):
        tree[i] = tree[i * 2] * tree[i * 2 + 1]

    return tree


def update(tree, index, value):
    if value > 0:
        value = 1
    elif value == 0:
        value = 0
    elif value < 0:
        value = -1

    tree[index] = value
    index //= 2

    while index > 0:
        tree[index] = tree[index * 2] * tree[index * 2 + 1]
        index //= 2


def query(tree, start_index, end_index):
    result = 1
    global answer

    while start_index <= end_index:
        if start_index % 2 == 1:
            result *= tree[start_index]
        if end_index % 2 == 0:
            result *= tree[end_index]

        start_index = (start_index + 1) // 2
        end_index = (end_index - 1) // 2

    if result == -1:
        answer += '-'
    elif result == 0:
        answer += '0'
    elif result == 1:
        answer += '+'


while True:
    try:
        n, m = map(int, sys.stdin.readline().split())
        nums = list(map(int, sys.stdin.readline().split()))
        k = ceil(log2(n))
        segment_tree = build_tree(nums, k)
        answer = ''

        for _ in range(m):
            command, a, b = sys.stdin.readline().split()
            a, b = int(a), int(b)
            if command == 'C':
                update(segment_tree, a + 2 ** k - 1, b)
            elif command == 'P':
                query(segment_tree, a + 2 ** k - 1, b + 2 ** k - 1)

        print(answer)

    except:
        break