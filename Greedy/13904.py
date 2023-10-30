# 점수가 높은 것부터 하나씩 살펴보기
# 최대한 늦게 풀 수 있도록 한다 -> deadline에 최대한 가깝게
import sys

n = int(sys.stdin.readline())
assignment = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

# 점수 기준 내림차순 정렬
assignment.sort(key=lambda x: -x[1])

# 날짜에 얻을 수 있는 최대 점수 기록
day = [0] * 1001

# 과제물 순회
for d, score in assignment:
    # 만약 0이면 점수 기록
    if day[d] == 0:
        day[d] = score
    # 0이 아니라면 -> 이미 기록된 점수가 있다면 그 날로부터 앞에 빈 날이 있는지 확인
    else:
        for i in range(d, 0, -1):
            if day[i] == 0:
                day[i] = score
                break

# 얻을 수 있는 점수 합계
print(sum(day[1:]))

# 7
# 4 100
# 2 10
# 1 20
# 2 50
# 5 99
# 5 99
# 5 99
# 447