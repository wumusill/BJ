import sys
import heapq

left_heap = []
right_heap = []
n = int(sys.stdin.readline())

for _ in range(n):
    num = int(sys.stdin.readline())
    if len(left_heap) == len(right_heap):
        heapq.heappush(left_heap, (-num, num))
    else:
        heapq.heappush(right_heap, num)

    if left_heap and right_heap:
        if left_heap[0][1] > right_heap[0]:
            left = heapq.heappop(left_heap)[1]
            right = heapq.heappop(right_heap)
            heapq.heappush(left_heap, (-right, right))
            heapq.heappush(right_heap, left)

    print(left_heap[0][1])

# 왼쪽은 최대 힙으로 중앙값보다 작은 값들이 들어감
# 오른쪽은 최소 힙으로 중앙값보다 큰 값들이 들어감
# 왼쪽 힙의 최댓값은 항상 중앙값이 됨

# 길이가 같다면 왼쪽에 수를 넣는다 길이가 같지 않다면 길이를 맞춰주기 위해 오른쪽에 수를 넣는다.
# 만약에 왼쪽 첫번째 값이 오른쪽 첫번째보다 크면 바꿔준다.
# 왼쪽은 중간값을 기준으로 작은 수가 들어가는데 왼쪽 첫 값이 크다면 중간값보다 큰 값이 왼쪽에 있는 상황