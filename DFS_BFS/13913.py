from collections import deque
import sys

n, k = map(int, sys.stdin.readline().rstrip().split())
queue = deque()
visited = [-1] * 100001

visited[n] = 1
queue.append((n, 1))

while queue:
    x, dist = queue.popleft()

    if x == k:
        print(dist - 1)
        break

    for next in [x + 1, x - 1, x * 2]:
        # 숨바꼭질 시리즈 문제에서 항상 런타임 에러를 유발했던 범위 설정
        if 0 <= next <= 100000:
            if visited[next] == -1:
                visited[next] = dist + 1
                queue.append((next, dist + 1))

# 가는 방법을 출력하기 위한 반복문
# 여기도 런타임 에러를 방지하기 위한 범위 설정
track = deque([k])
while k != n:
    if k + 1 <= 100000 and visited[k + 1] == visited[k] - 1:
        k += 1
    elif k - 1 <= 100000 and visited[k - 1] == visited[k] - 1:
        k -= 1
    elif k // 2 <= 100000 and k % 2 == 0 and visited[k // 2] == visited[k] - 1:
        k //= 2
    track.appendleft(k)

print(*track)