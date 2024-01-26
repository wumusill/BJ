# 행렬 최대 1,500 by 1,500인데 무식하게 돌려도 시간 초과 안 나지 않을까 했으나 메모리 초과
import sys
import heapq

n = int(sys.stdin.readline())
l = []
for _ in range(n):
    a = list(map(lambda x: -int(x), sys.stdin.readline().split()))
    l += a

heapq.heapify(l)

for i in range(n):
    num = heapq.heappop(l)

print(-num)
##########################################################################################
# 어차피 n번째 큰 수만 필요하니 그 이하는 저장하지 않고 다 날리자 : 1808ms
import sys
import heapq

n = int(sys.stdin.readline())
h = []

# 입력 받은 리스트의 원소를 전부 힙에 넣고
for _ in range(n):
    for num in list(map(int, sys.stdin.readline().split())):
        heapq.heappush(h, num)

    # 큰 수 n개만 남기고 다 제거
    while len(h) > n:
        heapq.heappop(h)

print(h[0])
##########################################################################################
# heappush + heappop 보다 heappushpop을 활용 : 1020ms
import sys
import heapq

n = int(sys.stdin.readline())
h = []

# 입력 받은 리스트의 원소를
for _ in range(n):
    for num in list(map(int, sys.stdin.readline().split())):
        # 힙에 원소의 개수가 n보다 작으면 넣기만 하고
        if len(h) < n:
            heapq.heappush(h, num)
        # n보다 크거나 같으면 원소를 넣고 힙의 최솟값 제거해서 항상 n개의 원소 유지
        else:
            heapq.heappushpop(h, num)

print(h[0])