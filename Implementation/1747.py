import sys

n = int(sys.stdin.readline())


# 팰린드롬 판별하는 함수
def palindrome(num):
    for i in range(len(num)-1, -1, -1):
        if num[i] != num[len(num) - i - 1]:
            return False
    else:
        return True


# 범위가 문제에 제시되어 있지 않아 임의로 설정
prime = [True for _ in range(2000001)]
prime[0], prime[1] = False, False
for i in range(2, int(2000000 ** 0.5) + 1):
    if prime[i]:
        for j in range(i * 2, 2000001, i):
            prime[j] = False

for i in range(n, 2000001):
    if palindrome(str(i)) and prime[i]:
        print(i)
        break
####################################################################
# 위 코드보다 더 빠름
# 정답 처리 받긴 했으나 수의 범위를 임의로 200만으로 설정
# 수의 범위를 따로 설정할 필요 없는 아래 코드
import sys

n = int(sys.stdin.readline())


# 팰린드롬 판별 함수
def palindrome(num):
    for i in range(len(num)-1, -1, -1):
        if num[i] != num[len(num) - i - 1]:
            return False
    else:
        return True


# 소수 판별 함수
def prime(num):
    if num == 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


# 답이 나올 때까지 수를 탐색하기 때문에 따로 범위 설정 필요 없음
while True:
    if palindrome(str(n)) and prime(n):
        print(n)
        break
    else:
        n += 1