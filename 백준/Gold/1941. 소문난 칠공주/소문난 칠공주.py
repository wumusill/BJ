import sys
from itertools import combinations
from collections import deque

mat = [list(sys.stdin.readline().rstrip()) for _ in range(5)]
c = combinations([i for i in range(25)], 7)
potential = []
answer = 0

for sample in c:
    cnt = {'S': 0, 'Y': 0}
    for element in sample:
        x, y = element // 5, element % 5
        cnt[mat[x][y]] += 1
        if cnt['Y'] == 4:
            break
    else:
        potential.append(sample)


def bfs(q, sample, visited):
    global answer
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    v = 0

    while q:
        num = q.popleft()
        x, y = num // 5, num % 5
        v += 1
        if v == 7:
            answer += 1
            break

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or ny < 0 or nx > 4 or ny > 4:
                continue
            if (nx * 5 + ny) in sample and visited[nx][ny]:
                visited[nx][ny] = False
                q.append((nx * 5 + ny))


for sample in potential:
    q = deque([])
    visited = [[True for _ in range(5)] for _ in range(5)]
    q.append(sample[0])
    visited[sample[0] // 5][sample[0] % 5] = False
    bfs(q, sample, visited)


print(answer)

# 아래가 모범 답안 #######################################################
# 델타
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

# 백트레킹
# 도연 yc 갯수
def backtracking(yc, lev=1):
  global ans
    
  # 두 가지 종료 조건
  # 도연이 4 이상인 경우 안되는 조합임
  if yc >= 4:
    return
  # lev가 7이면 조합 완성됨
  if lev == 7:
    c_dir_arr = [*dir_arr]
    c_dir_arr.sort()                   # 정렬하는 이유: 튜플은 순서가 다르면 서로 다른 것, 집합에 튜플을 넣을건데 같은 원소로 이루어져 있으면 제거될 수 있도록 하기 위함
    ans.add(tuple(c_dir_arr))          # 튜플로 변환해서 ans(set)에 넣는 이유: 리스트는 set에 넣을 수 없음
    return                             # 집합의 원소는 hashable 해야 한다
                                       # hasbable: 같은 객체는 항상 같은 해시값을 가져야 한다. 해시값은 객체의 생명주기 동안 절대 바뀌면 안된다
  # 조합 이어가기                         # list의 원소는 변경 가능(mutable)하기 때문에 hashable 하지 않음, 튜플은 변경 불가능(immuatble)하여 hashable함
  # 현재까지 만들어진 조합 반복문 돌리기
  for x, y in dir_arr:
    # 4방향 무빙
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if nx >= 0 and ny >= 0 and nx < 5 and ny < 5 and not visited[ny][nx]:
        visited[ny][nx] = True
        dir_arr.append((nx, ny))
        # 도연파면 yc + 1 해주기
        if map_arr[ny][nx] == 'Y':
          backtracking(yc+1, lev+1)
        else:
          backtracking(yc, lev+1)
        visited[ny][nx] = False
        dir_arr.pop()


map_arr = [list(input()) for _ in range(5)]
visited = [[False] * 5 for _ in range(5)]

# 7개 좌표 배열
dir_arr = []

# 결과값(모든 경우의 수)
ans = set()

for y in range(5):
  for x in range(5):
    visited[y][x] = True
    # 좌표 담아주기
    dir_arr.append((x, y))
    # 도연파면 yc + 1 해주기
    if map_arr[y][x] == 'Y':
      backtracking(1)
    else:
      backtracking(0)
    # 좌표 원복
    dir_arr.pop()

print(len(list(ans)))
