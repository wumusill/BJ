from collections import deque
import sys
queue = deque()

n = int(sys.stdin.readline())
for _ in range(n):
    command = sys.stdin.readline().split()
    if command[0] == 'push_back':
        queue.append(int(command[1]))
    elif command[0] == 'push_front':
        queue.appendleft(int(command[1]))
    elif command[0] == 'pop_front':
        if queue:
            num = queue.popleft()
            print(num)
        else:
            print(-1)
    elif command[0] == 'pop_back':
        if queue:
            num = queue.pop()
            print(num)
        else:
            print(-1)
    elif command[0] == 'size':
        print(len(queue))
    elif command[0] == 'empty':
        if queue:
            print(0)
        else:
            print(1)
    elif command[0] == 'front':
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif command[0] == 'back':
        if queue:
            print(queue[-1])
        else:
            print(-1)