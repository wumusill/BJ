from collections import deque
import sys

queue = deque([1])
n = int(sys.stdin.readline())
answer = []

visited = [False] * (n + 1)
distance = [1] * (n + 1)
visited[1] = True

# 최솟값 출력을 위한 BFS
while queue:
    x = queue.popleft()
    if x * 3 <= n and not visited[x * 3]:
        visited[x * 3] = True
        queue.append(x * 3)
        distance[x * 3] = distance[x] + 1
    if x * 2 <= n and not visited[x * 2]:
        visited[x * 2] = True
        queue.append(x * 2)
        distance[x * 2] = distance[x] + 1
    if x + 1 <= n and not visited[x + 1]:
        visited[x + 1] = True
        queue.append(x + 1)
        distance[x + 1] = distance[x] + 1

print(distance[n] - 1)
answer.append(n)

# 최솟값이 되는 과정 출력을 위한 반복문
while n != 1:
    # n이 3으로 나누어 떨어지고, 거리 차가 1이라면
    if n % 3 == 0 and distance[n // 3] == distance[n] - 1:
        n //= 3
        answer.append(n)
    elif n % 2 == 0 and distance[n // 2] == distance[n] - 1:
        n //= 2
        answer.append(n)
    else:
        n -= 1
        answer.append(n)

print(*answer)