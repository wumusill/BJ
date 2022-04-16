from collections import deque
import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    priority = list(map(int, input().split()))
    queue = deque()

    for i in range(n):
        queue.append((i, priority[i]))

    priority.sort()
    max_priority = priority.pop()
    order = 0

    while queue:
        a = queue.popleft()
        target = a[0]
        target_priority = a[1]

        if target_priority == max_priority:
            order += 1
            if target == m:
                print(order)
                break
            max_priority = priority.pop()
        else:
            queue.append(a)
#################################################################################

from collections import deque
import sys

input = sys.stdin.readline
queue = deque()

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    priority = list(map(int, input().split()))
    index = [i for i in range(n)]
    order = 0

    while priority:
        if priority[0] == max(priority):
            order += 1
            if index[0] == m:
                print(order)
                break
            priority.pop(0)
            index.pop(0)
        else:
            priority.append(priority.pop(0))
            index.append(index.pop(0))