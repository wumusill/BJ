import sys

string = list(sys.stdin.readline())
stack = []

for s in string:
    if s == '(':
        stack.append(s)
    elif s == ')':
        if (not stack) or (stack and stack[-1] != '('):
            stack.append(s)
        elif stack and stack[-1] == '(':
            stack.pop()

print(len(stack))