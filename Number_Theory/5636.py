import sys

prime = [True] * 100001
prime[0] = False
prime[1] = False

for i in range(2, 100001):
    if prime[i]:
        for j in range(i * 2, 100001, i):
            prime[j] = False

while True:
    n = sys.stdin.readline().strip()
    if n == '0':
        break
    else:
        ans = 0
        for i in range(len(n)):
            for j in range(i + 1, len(n)):
                num = int(n[i:j])
                if num > 100000:
                    continue
                if prime[num] and num > ans:
                    ans = num
        print(ans)