import sys
from collections import deque
queue = deque()
input = sys.stdin.readline      # 이 코드 추가 후 시간 초과 X  이 코드를 습관화 하자

# 시간 초과
n = int(input())
for _ in range(n):
    command = input().split()
    if command[0] == 'push':
        queue.append(int(command[1]))
    elif command[0] == 'pop':
        if len(queue) != 0:
            num = queue.popleft()
            print(num)
        else:
            print(-1)
    elif command[0] == 'size':
        print(len(queue))
    elif command[0] == 'empty':
        print(1 if len(queue) == 0 else 0)
    elif command[0] == 'front':
        print(queue[0] if len(queue) != 0 else -1)
    elif command[0] == 'back':
        print(queue[-1] if len(queue) != 0 else -1)