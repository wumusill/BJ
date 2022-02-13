import sys
from itertools import product

n = int(sys.stdin.readline())

for _ in range(n):
    k = int(sys.stdin.readline())
    answer = 1
    dict = {}
    for i in range(k):
        type = sys.stdin.readline().split()[1]

        # 옷 종류 별 갯수 사전에 추가
        if type in dict.keys():
            dict[type] += 1
        else:
            dict[type] = 1

    # 안 입는 경우 (1) 더해서 종류별 경우의 수 구하기
    for j in dict.values():
        answer *= (j+1)

    # 다 벗는 경우 제외
    print(answer-1)