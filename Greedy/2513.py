# 가장 멀리 있는 학생부터 최대한 많이 태워오기
# 메모리 초과
import sys

n, limit, school = map(int, sys.stdin.readline().split())
left = []
right = []

for _ in range(n):
    x, num = map(int, sys.stdin.readline().split())
    dist = x - school
    if dist < 0:
        for _ in range(num):
            left.append(abs(dist))
    else:
        for _ in range(num):
            right.append(abs(dist))

left.sort()
right.sort()

ans = 0
for i in range(len(left) - 1, -1, -limit):
    ans += left[i] * 2
for i in range(len(right) - 1, -1, -limit):
    ans += right[i] * 2

print(ans)
##############################################################################################
import sys

n, k, school = map(int, sys.stdin.readline().split())

# 학교 기준 왼쪽 오른쪽 분리해서 저장
left = []
right = []

for _ in range(n):
    x, num = map(int, sys.stdin.readline().split())
    d = x - school
    if d < 0:
        left.append([abs(d), num])
    else:
        right.append([abs(d), num])

# 거리 기준 오름차순 정렬
left.sort(key=lambda x: x[0])
right.sort(key=lambda x: x[0])

ans = 0
while right:
    limit, distance = k, 0
    # 버스가 다 찰 때까지
    while limit > 0 and right:
        # 가장 먼 곳 방문
        dist, student = right.pop()

        # 남은 자리에 학생을 다 태울 수 있으면 태우고 남은 자리 갱신
        if limit >= student:
            limit -= student

        # 자리가 없는데 남은 학생이 있으면
        else:
            # 남은 학생 저장
            right.append([dist, student - limit])
            # 자리 없으므로 while문 탈출
            limit = 0

        # 가장 먼 거리 저장
        distance = max(dist, distance)
    # 저장된 가장 먼 거리 왕복 합산
    ans += distance * 2

while left:
    limit, distance = k, 0
    while limit > 0 and left:
        dist, student = left.pop()
        if limit >= student:
            limit -= student
        else:
            left.append([dist, student - limit])
            limit = 0
        distance = max(dist, distance)
    ans += distance * 2

print(ans)

# 2 1 3
# 1 1
# 2 2
# 8