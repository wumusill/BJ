import sys
import heapq

n = int(sys.stdin.readline())
answer = [0] * (n + 1)

# 강의실 (시작 시간, 종료 시간) 기준 오름차순 정렬
lectures = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
lectures.sort(key=lambda x: (x[1], x[2]))

# 힙은 종료 시간 기준 가장 빠른순 (최소 힙)
h, new_room = [], 1
for class_num, start, end in lectures:
    while h and h[0][0] <= start:                               # 시작 전 종료된 강의가 있으면
        before_class, classroom = heapq.heappop(h)
        heapq.heappush(h, (end, classroom))                     # 그 강의실 배정
        answer[class_num] = classroom
        break

    # 힙이 비었거나, 강의실이 가득 차있으면 새 강의실 오픈 (종료 시간, 새 강의실)
    else:
        heapq.heappush(h, (end, new_room))
        answer[class_num] = new_room
        new_room += 1

print(max(answer[1:]))
for res in answer[1:]:
    print(res)