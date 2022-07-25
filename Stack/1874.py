from collections import deque
import sys

stack = deque()
n = int(sys.stdin.readline())
answer = []
res = True
num_list = deque([i for i in range(1, n + 1)])

for _ in range(n):
    num = int(sys.stdin.readline())
    while res:
        if stack and stack[-1] == num:
            stack.pop()
            answer.append("-")
            break
        if stack and not num_list and stack[-1] != num:
            res = False
            break
        popleft = num_list.popleft()
        stack.append(popleft)
        answer.append("+")

if res:
    for j in answer:
        print(j)
else:
    print("NO")