import sys
import heapq

t = int(sys.stdin.readline())
for _ in range(t):
    k = int(sys.stdin.readline())
    max_heap = []
    min_heap = []
    visited = [False] * k
    for id in range(k):
        cmd, num = sys.stdin.readline().split()
        if cmd == 'I':
            heapq.heappush(min_heap, (int(num), id))
            heapq.heappush(max_heap, (-int(num), id))
            # True이면 어떤 힙에서도 삭제되지 않은 상태
            visited[id] = True
        elif cmd == 'D' and num == '1':
            # visited == False 일 때 -> 해당 노드가 다른 노드에서 삭제되었다는 것이므로 다 삭제해준다.
            while max_heap and not visited[max_heap[0][1]]:
                heapq.heappop(max_heap)
            if max_heap:
                visited[max_heap[0][1]] = False
                heapq.heappop(max_heap)
        elif cmd == 'D' and num == '-1':
            while min_heap and not visited[min_heap[0][1]]:
                heapq.heappop(min_heap)
            if min_heap:
                visited[min_heap[0][1]] = False
                heapq.heappop(min_heap)

    # 모든 연산이 끝난 후에도 삭제된 노드가 들어있을 수 있으므로, 한번 더 확인한다.
    while min_heap and not visited[min_heap[0][1]]:
        heapq.heappop(min_heap)
    while max_heap and not visited[max_heap[0][1]]:
        heapq.heappop(max_heap)

    if min_heap and max_heap:
        print(-max_heap[0][0], min_heap[0][0])
    else:
        print('EMPTY')