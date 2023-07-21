import sys

prime_num = [True] * 1000001
prime_num[0] = False
prime_num[1] = False

for i in range(2, 1000001):
    if prime_num[i]:
        for j in range(i * 2, 1000001, i):
            prime_num[j] = False

while True:
    n = int(sys.stdin.readline())
    if n == 0:
        break
    for i in range(3, n, 2):
        if prime_num[i] and prime_num[n - i]:
            print(f"{n} = {i} + {n - i}")
            break
    else:
        print("Goldbach's conjecture is wrong.")
