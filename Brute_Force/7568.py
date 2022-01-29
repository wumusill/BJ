import sys
# 반례가 뭘까 아쉽네
n = int(input())

# 리스트 원본
l = []
for _ in range(n):
    w, h = map(int, sys.stdin.readline().split())
    l.append((w, h))

# 몸무게 순으로 정렬
sort_w = sorted(l, reverse=True, key=lambda x: x[0])

# 등수를 기록하기 위한 사전
dict = {}

order = 1

for i in range(1, len(sort_w)):
    # 몸무게 순 정렬 리스트에서 앞사람이 키도 크다면 1등, 등 수 1 올림
    if sort_w[i-1][1] > sort_w[i][1]:
        dict[sort_w[i-1]] = order
        order += 1
    # 몸무게는 나가는데 키가 작다면 그냥 등수 부여
    else:
        dict[sort_w[i-1]] = order

# 몸무게 순 정렬 리스트 마지막에 있는 데이터를 처리하기 위한 작업
# 앞사람 보다 몸무게, 키 둘다 작다면 꼴등 부여
if sort_w[-2][0] > sort_w[-1][0] and sort_w[-2][1] > sort_w[-1][1]:
    dict[sort_w[-1]] = len(sort_w)
# 둘 중 하나만 크다면 앞사람 등수 부여
else:
    dict[sort_w[-1]] = order

# 사전을 돌면서 원본 리스트의 순서대로 부여된 등수 출력
for tup in l:
    print(dict[tup], end=' ')

# 자기 보다 키, 몸무게 둘다 큰 사람의 명 수를 확인
n = int(input())
people = []
for _ in range(n):
    w, h = map(int, sys.stdin.readline().split())
    people.append((w, h))

for person in people:
    rank = 1
    for other_person in people:
        if person == other_person:
            continue
        if other_person[0] > person[0] and other_person[1] > person[1]:
            rank += 1
    print(rank, end=' ')