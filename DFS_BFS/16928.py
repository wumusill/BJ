from collections import deque
import sys

queue = deque([1])
n, m = map(int, sys.stdin.readline().rstrip().split())
answer = [0] * 101

# 뱀과 사다리 기록할 dict
ladder = {}
snake = {}

# 사다리 기록
for _ in range(n):
    u, v = map(int, sys.stdin.readline().rstrip().split())
    ladder[u] = v

# 뱀 기록
for _ in range(m):
    u, v = map(int, sys.stdin.readline().rstrip().split())
    snake[u] = v

dice = [1, 2, 3, 4, 5, 6]

while queue:
    # 현재 위치
    now = queue.popleft()
    for num in dice:
        next = now + num
        # next가 방문 가능하지만 방문을 하지 않았다면
        if next <= 100 and answer[next] == 0:
            # 만약 next에 사다리가 연결됐다면 이동
            if next in ladder.keys():
                next = ladder[next]
            # 만약 next에 뱀이 연결됐다면 이동
            elif next in snake.keys():
                next = snake[next]
            # 방문한적이 없는 곳이라면 방문 처리
            if answer[next] == 0:
                answer[next] = answer[now] + 1
                queue.append(next)

print(answer[100])