import sys
import heapq

t = int(sys.stdin.readline())
for _ in range(t):
    k = int(sys.stdin.readline())
    h = list(map(int, sys.stdin.readline().split()))

    # 입력 받은 리스트 힙으로 변환
    heapq.heapify(h)

    # 비용이 가장 작은 두 개를 합쳐서 다시 힙에 삽입
    # 힙에 남은 파일이 없을 때까지 반복
    ans = 0
    while True:
        a = heapq.heappop(h)
        b = heapq.heappop(h)
        ans += a + b

        if not h:
            print(ans)
            break
        else:
            heapq.heappush(h, (a + b))