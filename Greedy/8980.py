# 목적지가 가까운 택배를 최대한 많이 옮김
import sys

n, c = map(int, sys.stdin.readline().split())
m = int(sys.stdin.readline())
box = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]

# 도착지 기준 오름차순 정렬
box.sort(key=lambda x: x[1])
max_cnt = [c] * (n + 1)
answer = 0

for x, y, z in box:
    minimum = c                             # 트럭의 박스 최대 수용량
    for i in range(x, y):                   # x 마을부터 y 이전 마을까지 순회
        minimum = min(minimum, max_cnt[i])  # i 번째 마을을 지날 수 있는 box의 양 갱신
    minimum = min(minimum, z)               # 목적지까지의 모든 마을을 지날 수 있는 box만큼 트럭에 싣기
    for i in range(x, y):
        max_cnt[i] -= minimum               # 트럭에 실은 만큼 마을을 지날 수 있는 box의 수 차감
    answer += minimum                       # 옮긴 box의 전체 양 갱신

print(answer)