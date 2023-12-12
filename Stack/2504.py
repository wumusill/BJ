import sys

string = sys.stdin.readline().rstrip()
stack = []

for s in string:
    # 스택에 추가
    stack.append(s)

    # 숫자로 변경하는 조건문
    if len(stack) > 1:
        if stack[-2] == '(' and stack[-1] == ')':
            stack.pop()
            stack.pop()
            stack.append(2)

        elif stack[-2] == '[' and stack[-1] == ']':
            stack.pop()
            stack.pop()
            stack.append(3)

    # 곱셈 처리
    if len(stack) > 2:
        if stack[-3] == '(' and stack[-1] == ')' and type(stack[-2]) == int:
            stack.pop()
            res = stack.pop()
            stack.pop()
            stack.append(res * 2)

        elif stack[-3] == '[' and stack[-1] == ']' and type(stack[-2]) == int:
            stack.pop()
            res = stack.pop()
            stack.pop()
            stack.append(res * 3)

    # 덧셈 처리
    if len(stack) > 1 and type(stack[-1]) == int and type(stack[-2]) == int:
        res = stack[-1] + stack[-2]
        stack.pop()
        stack.pop()
        stack.append(res)

# 정상 스택
try:
    print(sum(stack))

# 비정상 스택
except:
    print(0)