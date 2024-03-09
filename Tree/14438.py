# update와 query 함수의 기능을 solution 이라는 하나의 함수로 구현하다가 디버깅과 코드 수정에 많은 시간 소요 -> 가독성도 좋지 않았음
# 하나의 함수는 하나의 기능만 할 수 있도록 하자 -> 가독성도 좋고 코드 수정과 디버깅이 훨씬 수월
import sys
from math import log2, ceil


def update(tree, index, value):
    tree[index] = value
    index //= 2
    while index:
        tree[index] = min(tree[index * 2], tree[index * 2 + 1])
        index //= 2


def query(tree, start_index, end_index):
    result = float('inf')

    while start_index <= end_index:
        if start_index % 2 == 1:
            result = min(result, tree[start_index])
        if end_index % 2 == 0:
            result = min(result, tree[end_index])

        start_index = (start_index + 1) // 2
        end_index = (end_index - 1) // 2

    return result


def build_segment_tree(nums, k):
    tree_size = 2 ** (k + 1)
    tree = [0] * tree_size

    for idx, num in enumerate(nums):                            # 리프 노드에 숫자 입력하는 반복문
        idx += 2 ** k
        tree[idx] = num

    for i in range(2 ** k - 1, -1, -1):                         # 부모 노드 데이터를 갱신하는 반복문
        tree[i] = min(tree[i * 2], tree[i * 2 + 1])

    return tree


n = int(sys.stdin.readline())
k = ceil(log2(n))
nums = list(map(int, sys.stdin.readline().split()))

segment_tree = build_segment_tree(nums, k)

m = int(sys.stdin.readline())
for _ in range(m):
    operation, b, c = map(int, sys.stdin.readline().split())
    if operation == 1:
        idx = b + 2 ** k - 1
        update(segment_tree, idx, c)
    elif operation == 2:
        start_idx, end_idx = b + (2 ** k - 1), c + (2 ** k - 1)
        result = query(segment_tree, start_idx, end_idx)
        print(result)