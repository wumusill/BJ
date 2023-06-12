import sys


string = sys.stdin.readline().strip()
stack = []
ans = []
idx = 0
while idx < len(string):
    if string[idx] == '<':
        while string[idx] != '>':
            ans.append(string[idx])
            idx += 1
        ans.append(string[idx])
        idx += 1
    else:
        while idx < len(string) and string[idx] != '<':
            if string[idx] == ' ':
                while stack:
                    ans.append(stack.pop())
                ans.append(' ')
                idx += 1
            stack.append(string[idx])
            idx += 1
        while stack:
            ans.append(stack.pop())

print(''.join(ans))