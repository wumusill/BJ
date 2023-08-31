import heapq
import sys

n = int(sys.stdin.readline())
classroom = []

# 강의 번호, 시작 시간, 종료 시간 : 강의 번호는 필요 없으므로 [1:]
# 강의 시작 시간 기준 오름차순 정렬, 시작 시간이 동일하면 종료 시간 기준 오름차순 정렬
lecture_l = [list(map(int, sys.stdin.readline().split()[1:])) for _ in range(n)]
lecture_l.sort(key=lambda x: (x[0], x[1]))

# 힙에 가장 먼저 시작하는 강의의 종료 시간 추가
heapq.heappush(classroom, lecture_l[0][1])

# 두 번째 강의부터 순회
# 다음 강의 시작 시간이 이전 강의 중 가장 빨리 끝나는 강의 종료 시간보다 크거나 같다면
# 가장 빨리 끝나는 강의실에 강의 배정 -> 최소 힙에서 이전 강의 종료 시간 pop 후 현재 강의 종료 시간 push
# 만약 현재 강의 종료 시간이 가장 빨리 끝나는 강의보다 일찍 시작한다면 그냥 새로운 강의실 사용
for i in range(1, n):
    start, end = lecture_l[i][0], lecture_l[i][1]
    if start >= classroom[0]:
        heapq.heappop(classroom)
    heapq.heappush(classroom, end)

print(len(classroom))