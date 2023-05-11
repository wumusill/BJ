# 리스트의 최댓값이 가운데 위치, 정규화된 모양을 띄면 된다.
# 입력 받은 리스트를 내림차순으로 정렬
# 앞뒤로 번갈아가면서 삽입하면 됨
import sys
from collections import deque

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())

    # 내림차순 정렬
    l = sorted(map(int, sys.stdin.readline().split()), reverse=True)

    # 앞뒤로 삽입하기 위해 deque 활용
    q = deque()
    for i in range(n):
        # 앞뒤 번갈아가면서 삽입
        if i % 2 == 0:
            q.appendleft(l[i])
        else:
            q.append(l[i])

    # 마지막과 첫 원소도 연결된 것으로 보기 때문에 차이를 계산
    ans = abs(q[-1] - q[0])

    # q를 순회하면서 인접한 원소의 차이를 계산
    for i in range(1, n):
        ans = max(ans, abs(q[i] - q[i - 1]))
    print(ans)