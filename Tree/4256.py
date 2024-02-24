# 까먹어서 다시 왔다면 그림을 그리고 잘 생각해볼 것
import sys
from collections import deque

sys.setrecursionlimit(10**6)


def postorder(pre_s, pre_e, in_s, in_e):
    global answer
    if pre_s > pre_e or in_s > in_e:
        return

    val = preorder[pre_s]
    idx = inorder_idx[val]

    # 내가 처음 구현한 재귀 : 오른쪽 서브 트리 갔다가 왼쪽 서브 트리 재귀할 때 문제 발생
    # 중위에서 오른쪽 순회를 마지막에 하므로 오른쪽 서브 트리의 값들은 index가 큼
    # 이를 다시 왼쪽 서브 트리로 재귀할 경우 index 범위가 전체 list 길이를 초과하는 문제 발생
    # 아래 코드처럼 중위 시작(in_s)을 빼주면 됨
    # postorder(pre_s + 1, pre_s + idx, in_s, in_s + idx - 1)  # left
    # postorder(pre_s + idx + 1, pre_e, idx + 1, in_e)         # right

    # 왼쪽 서브 트리 (전위 왼쪽 서브 첫 idx, 전위 왼쪽 서브 마지막 idx, 중위 왼쪽 서브 첫 idx, 중위 왼쪽 서브 마지막 idx)
    postorder(pre_s + 1, pre_s + idx - in_s, in_s, idx - 1)

    # 오른쪽 서브 트리 (전위 오른쪽 서브 첫 idx, 전위 오른쪽 서브 마지막 idx, 중위 오른쪽 서브 첫 idx, 중위 오른쪽 서브 마지막 idx)
    postorder(pre_s + idx - in_s + 1, pre_e, idx + 1, in_e)

    # print(val, end=' ') -> 출력 형식 에러 유발
    answer.append(val)


t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    preorder = deque(list(map(int, sys.stdin.readline().split())))
    inorder = list(map(int, sys.stdin.readline().split()))

    # inorder 에서 원소의 index를 찾기 위함
    inorder_idx = {val:idx for idx, val in enumerate(inorder)}
    answer = []
    postorder(0, n - 1, 0, n - 1)
    print(*answer)