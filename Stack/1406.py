import sys
from collections import deque

stack = list(sys.stdin.readline().strip())
q = deque()

n = int(sys.stdin.readline())

for _ in range(n):
    command = sys.stdin.readline().strip()
    letter = None
    if len(command) != 1:
        command, letter = command.split()

    if command == 'L' and stack:
        letter = stack.pop()
        q.appendleft(letter)
    elif command == 'D' and q:
        letter = q.popleft()
        stack.append(letter)
    elif command == 'B' and stack:
        stack.pop()
    elif command == 'P':
        stack.append(letter)

print(''.join(stack) + ''.join(q))