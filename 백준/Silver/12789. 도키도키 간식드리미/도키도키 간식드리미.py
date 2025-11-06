import sys
from collections import deque

n = int(sys.stdin.readline().strip())
order = deque(list(map(int, sys.stdin.readline().split())))
wait = []
i, t = 0, 1

while i < n:
    x = order[i]
    if x == t:
        t += 1
        i += 1
    elif wait and wait[-1] == t:
        wait.pop()
        t += 1
    else:
        wait.append(x)
        i += 1
    continue

while wait:
    x = wait.pop()
    if x == t:
        t += 1
    else:
        print('Sad')
        break
else:
    print('Nice')