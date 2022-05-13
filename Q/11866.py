from collections import deque

queue = deque()
n, k = map(int, input().split())
visited = [0] * (n+1)
temp = 0

while True:
    for i in range(1, n+1):
        if visited[i] == 0:
            temp += 1
        else:
            continue
        if temp == k:
            queue.append(i)
            visited[i] = 1
            temp = 0

    if len(queue) == n:
        break
print('<', end='')
while queue:
    print(queue.popleft(), end='')
    if queue:
        print(', ', end='')
print('>')


# 다른 사람 코드 약 1/5
n, k = map(int, input().split())
arr = [i for i in range(1, n+1)]
res = []
i = k-1
while len(res) < n:
    if i >= len(arr):
        i = i % len(arr)
    else:
        res.append(str(arr.pop(i)))
        i += k - 1

print('<', ', '.join(res), '>', sep='')