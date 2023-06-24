import sys

n = int(sys.stdin.readline())
num = [sys.stdin.readline().strip() for _ in range(n)]

# 원소들을 뒤에서부터 한 글자씩 순회
idx = -1

# index가 맨 앞으로 도달할 때까지 순회
while idx >= -len(num[0]):
    # 이미 나온 글자들을 기록
    part_nums = []
    for i in range(n):
        # 뒤에서 부터 슬라이싱
        part_num = num[i][idx:]
        # 이미 나온 글자라면 한 글자를 추가해서 다시 순회
        if part_num in part_nums:
            idx -= 1
            break
        # 처음 등장한 글자라면 리스트에 기록하고 다음 원소 탐색
        part_nums.append(part_num)
    # for 문이 끝까지 다 돌았다면 -> 모든 원소들의 부분 글자가 고유값, 중복이 없다면 정답 출력
    else:
        print(-idx)
        break