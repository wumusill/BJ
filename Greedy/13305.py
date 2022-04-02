import sys

N = int(sys.stdin.readline())
distance = list(map(int, sys.stdin.readline().split()))
price = list(map(int, sys.stdin.readline().split()))

answer = distance[0] * price[0]
min_price = price[0]

# min_price = min(price[:-1])
# idx_min_price = price.index(min_price)
# dist_min_price = idx_min_price
#
# answer += min_price * sum(distance[idx_min_price:])
#
# while dist_min_price != 0:
#     min_price = min(price[:dist_min_price])
#     idx_min_price = dist_min_price
#     dist_min_price = price.index(min_price)
#
#     answer += min_price * sum(distance[dist_min_price:idx_min_price])
#
# print(answer)

for i in range(1, N-1):
    if price[i] < min_price:
        min_price = price[i]
    answer += min_price * distance[i]

print(answer)

# 5
# 2 3 1 1
# 5 2 4 1 1
# 19