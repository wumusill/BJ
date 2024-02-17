# 신발끈 공식 : https://namu.wiki/w/%EC%8B%A0%EB%B0%9C%EB%81%88%20%EA%B3%B5%EC%8B%9D
import sys

n = int(sys.stdin.readline())
x, y = [], []

for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    x.append(a)
    y.append(b)

x.append(x[0])
y.append(y[0])


def solution(x, y):
    s = 0
    for i in range(1, len(x)):
        s += x[i - 1] * y[i]
        s -= y[i - 1] * x[i]

    return abs(s / 2)


print(round(solution(x, y), 1))