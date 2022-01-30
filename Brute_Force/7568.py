import sys

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