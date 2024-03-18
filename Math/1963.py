# 숫자를 한 자리씩 변경
# 변경한 숫자가 소수인지 판별
import sys
from collections import deque


def solution(num, target):
    q = deque([(num, 0)])
    visited = [True] * 10001

    while q:
        x, cnt = q.popleft()                                                # 현재 숫자, 번호 변경 횟수
        if x == target:                                                     # 현재 숫자가 목표 숫자와 같으면 변경 횟수 반환
            return cnt
        for idx, val in enumerate(list(map(int, list(str(x))))):
            i = abs(idx - 3)                                                # i : 자릿수, 무조건 4자리 수만 취급

            for p in range(1, 10 - val):                                    # 큰 숫자 탐색, 7이면 (8, 9)
                next = x + p * (10 ** i)                                    # 숫자 변경
                if 1000 < next < 10000:                                     # 변경된 숫자가 4자리 수이면서 (1000은 어차피 합성수)
                    if check[next] and visited[next]:                       # 변경된 숫자가 소수이면서 방문한적 없다면
                        q.append((next, cnt + 1))                           # 큐에 변경 횟수 갱신하여 함께 삽입
                        visited[next] = False                               # 숫자 방문 처리

            for m in range(1, val + 1):                                     # 작은 숫자 탐색, 3이면 (0, 1, 2)
                next = x - m * (10 ** i)
                if 1000 < next < 10000:
                    if check[next] and visited[next]:
                        q.append((next, cnt + 1))
                        visited[next] = False


n = int(sys.stdin.readline())
check = [True] * 10001                                                      # 소수 판별을 위한 에라토스테네스의 체 구현
for i in range(2, len(check)):
    if check:
        for j in range(i * 2, len(check), i):
            check[j] = False

for _ in range(n):
    n, t = map(int, sys.stdin.readline().split())
    print(solution(n, t))