# 메모리 초과 : 함수 파라미터로 리스트를 계속해서 넣은 것이 원인 -> 리스트를 넣지 않고 원소의 index를 파라미터로 활용
# index 메서드의 시간복잡도, O(N)로 인해 메모리 초과가 아니라도 시간 초과 예상
import sys


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, postorder: list[int], inorder: list[int]) -> Node:
        if inorder:
            idx = inorder.index(postorder.pop())

            node = Node(inorder[idx])
            node.right = self.buildTree(postorder, inorder[idx + 1:])
            node.left = self.buildTree(postorder, inorder[0:idx])

            return node


def preorder(node):
    if node is None:
        return
    print(node.val, end=' ')
    preorder(node.left)
    preorder(node.right)


n = int(sys.stdin.readline())
IN = list(map(int, sys.stdin.readline().split()))
POST = list(map(int, sys.stdin.readline().split()))

solution = Solution()
root = solution.buildTree(POST, IN)
preorder(root)

# 좀 더 복잡한 트리로 예시
# root = Node(1,
#             Node(2,
#                  Node(4),
#                  Node(5)),
#             Node(3,
#                  Node(6,
#                       Node(7,
#                            Node(9)),
#                       Node(8))))
#
#
# preorder(root)      # 전위 순회 결과 : [1, 2, 4, 5, 3, 6, 7, 9, 8]
# print()
# inorder(root)       # 중위 순회 결과 : [4, 2, 5, 1, 9, 7, 6, 8, 3]
# print()
# postorder(root)     # 후위 순회 결과 : [4, 5, 2, 9, 7, 8, 6, 3, 1]
#
# 전위, 중위 순회 결과물로 트리 구축
# 전위 순회 결과물의 첫 번째 값은 부모 노드
# 전위 순회 첫 번째 값(1)은 중위 순회 결과물을 정확히 왼쪽과 오른쪽으로 분할시키는 역할
# 전위 순회 두 번째 값(2)은 다시 중위 순회 결과를 반으로 가르고 4, 5가 각각 왼쪽 자식, 오른쪽 자식
# Divide Conquer 문제
#
# 후위, 중위 순회 결과물로 트리 구축도 마찬가지
# 후위 순회 결과물의 마지막 값은 부모 노드
# 후위 순회 마지막 값(1)은 중위 순회 결과물을 정확히 왼쪽과 오른쪽으로 분할시키는 역할
# 후위 순회 뒤에서 두 번째 값(3)은 중위 순회 결과물에서 왼쪽에만 값이 있음 -> 오른쪽 자식이 없다는 의미
# 후위 순회 뒤에서 세 번째 값(6)은 중위 순회 결과를 반으로 가르고 7과, 8이 각각 왼쪽 자식, 오른쪽 자식
#######################################################################################################################
import sys


sys.setrecursionlimit(int(1e9))


def preorder(in_s, in_e, post_s, post_e):
    if in_s > in_e or post_s > post_e:
        return

    # 부모 노드 출력
    p = POST[post_e]
    print(p, end=' ')

    # 서브 트리 분할 index
    left = IN_idx[p] - in_s
    right = in_e - IN_idx[p]

    # 왼쪽 서브 트리
    preorder(in_s, in_s + left - 1, post_s, post_s + left - 1)
    # 오른쪽 서브 트리
    preorder(in_e - right + 1, in_e, post_e - right, post_e - 1)


n = int(sys.stdin.readline())
IN = list(map(int, sys.stdin.readline().split()))
POST = list(map(int, sys.stdin.readline().split()))

# index 메서드를 사용하지 않고 inorder 결과물에서 원소의 index를 찾기 위함
IN_idx = {val : idx for idx, val in enumerate(IN)}
preorder(0, n - 1, 0, n - 1)