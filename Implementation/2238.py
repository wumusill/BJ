import sys

u, n = map(int, sys.stdin.readline().split())
auction = {i:[] for i in range(1, u + 1)}

# 금액 제시한 순서대로 이름 기록
for _ in range(n):
    name, price = sys.stdin.readline().rstrip().split()
    price = int(price)
    auction[price].append(name)

# 가장 적게 제시한 금액 기준 오름차순 정렬, 동률 시 가격 기준 오름차순 정렬
auction = sorted(auction.items(), key=lambda x: (len(x[1]), x))

# 1명 이상 제시한 금액 중 가장 먼저 제시한 사람과 금액 출력
for price, name in auction:
    if len(name) > 0:
        print(name[0], price)
        break

# 3 3
# a 1
# b 1
# c 1
# 출력 없음