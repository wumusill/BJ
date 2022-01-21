from math import sqrt
from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
m = int(sqrt(n))

if n == 1:
    print('')
else:
    l = [True] * n
    prime_num = deque()

    l[0] = False
    l[1] = False

    for i in range(2, m + 1):
        if l[i] == True:
            for j in range(i+i, n, i):
                l[j] = False

    for k in range(len(l)):
        if l[k] == True:
            prime_num.append(k)

    prime_num.append(n)

    while n != 1:
        i = prime_num.popleft()
        while n % i == 0:
            n /= i
            print(i)

#########################################################################
x = int(input())

while True:
    if x % 2:
        break
    else:
        print(2)
        x /= 2

i = 3

while x > 1:
    if x % i == 0:
        print(i)
        x /= i
    else:
        i += 2