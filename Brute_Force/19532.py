# n^2 시간복잡도
# n=2,000으로 최대 400만
# 시간 제한 1초인데 왜 시간 초과가 날까
# pypy3로 제출하면 통과
import sys

a, b, c, d, e, f = map(int, sys.stdin.readline().split())
breaker = False

for x in range(-999, 1000):
    for y in range(-999, 1000):
        res1 = a * x + b * y 
        res2 = d * x + e * y
        if res1 == c and res2 == f:
            print(x, y)
            breaker = True
            break
    if breaker:
        break


# 시간 초과 안나는 유사 풀이
a, b, c, d, e, f = map(int, input().split())

for x in range(-999, 1000):
    for y in range(-999, 1000):
        if a * x + b * y == c and d * x + e * y == f:
            print(x, y)


# 이것도 통과
import sys

a, b, c, d, e, f = map(int, sys.stdin.readline().split())

for x in range(-999, 1000):
    for y in range(-999, 1000): 
        if a * x + b * y == c and d * x + e * y == f:
            print(x, y)


# 연립 방정식 풀이
# a * x + b * y == c
# d * x + e * y == f
# x, y에 대한 식으로 정리하고 대입하면 아래 식 증명 가능
a, b, c, d, e, f = map(int, input().split())
x = int((c*e - b*f) / (a*e - b*d))
y = int((c*d - a*f) / (b*d - a*e))
print(x, y)