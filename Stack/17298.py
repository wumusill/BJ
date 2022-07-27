# 시간초과
# from collections import deque
# import sys
#
# n = int(sys.stdin.readline())
# nums = deque(list(map(int, sys.stdin.readline().split())))
# queue = deque()
# answer = deque()
# _max = max(nums)
#
# for i in range(n):
#     # 첫 값은 그냥 넣는다
#     if not queue:
#         queue.append(nums[i])
#         continue
#     # 만약 max 값이라면 오큰수는 존재하지 않으므로 -1
#     if queue[0] == _max:
#         queue.popleft()
#         answer.append(-1)
#     # 값이 큐의 첫 값보다 크다면 오큰수 이므로 popleft
#     while queue and nums[i] > queue[0]:
#         res = queue.popleft()
#         answer.append(nums[i])
#     # 값이 작다면 append
#     queue.append(nums[i])
#
# # 마지막 수는 오큰수가 존재하지 않음
# answer.append(-1)
#
# for j in answer:
#     print(j, end=' ')
############################################################################
from collections import deque
import sys

n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
stack = deque()

# 오큰수가 없는 -1로 초기화
answer = [-1] * n

for i in range(n):
    # stack 젤 위에 있는 index의 숫자가 현재 숫자보다 작다면 pop
    # pop한 idx에 현재 숫자 오큰수로 입력
    while stack and nums[stack[-1]] < nums[i]:
        idx = stack.pop()
        answer[idx] = nums[i]
    # 스택에 index push
    stack.append(i)

print(*answer)