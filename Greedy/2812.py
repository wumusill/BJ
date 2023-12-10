# 숫자를 순회하면서 스택에 삽입
# 만약 현재 순회 중인 숫자가 스택 마지막보다 크다면 pop
import sys

n, k = map(int, sys.stdin.readline().split())
nums = sys.stdin.readline().rstrip()

stack = []

for i in range(n):
    num = nums[i]
    # 앞 숫자 작으면 지울 수 있는 횟수만큼 제거
    while stack and k > 0 and int(stack[-1]) < int(num):
        stack.pop()
        k -= 1
    stack.append(num)

# 남은 k만큼 뒤 숫자 제거
if k > 0:
    print(int(''.join(stack[:-k])))
else:
    print(int(''.join(stack)))