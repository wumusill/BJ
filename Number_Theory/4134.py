# n부터 소수인지 아닌지 차례로 확인한다
# n을 2이상의 자연수로 나눠볼 때 n의 제곱근까지만 확인하는 방법
# 2 이상의 자연수로 나눠 떨어진다면 소수가 아니므로 다음 수 확인 (n + 1)
# 2 이상 제곱근 이하의 자연수로 나누어 떨어지지 않으면 소수
# 3432ms 풀이
import sys


k = int(sys.stdin.readline())
for _ in range(k):
    n = int(sys.stdin.readline())
    # 0 or 1은 무조건 2
    if n == 0 or n == 1:
        print(2)
        continue

    # 2 이상의 자연수로 나누기, 제곱근 설정
    res = 2
    sqrt = int(n ** 0.5)

    # 인수가 제곱근보다 작을 때까지 반복
    while res <= sqrt:
        # 만약 나누어 떨어진다면 다음 자연수를 확인, 제곱근 다시 세팅, 인수 초기화
        if n % res == 0:
            n += 1
            res = 2
            sqrt = int(n ** 0.5)

        # 인수로 나누어 떨어지지 않는다면 다음 인수
        else:
            res += 1

    # 결과 출력
    print(n)
############################################################################
# 836ms 를 보인 다른 분의 풀이
# 로직은 위와 똑같음
import math


# 함수 정의
def isPrime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    # 짝수면 False
    if n % 2 == 0:
        return False
    # 3부터 인수의 제곱근까지의 홀수 중 인수가 있는지 확인
    for i in range(3, int(math.sqrt(n)+1), 2):
        # 있으면 False
        if n % i == 0:
            return False
    # 없으면 True
    return True


t = int(input())
for _ in range(t):
    n = int(input())
    i = n
    # 함수가 True를 반환할 때 파라미터로 들어간 자연수를 출력
    # False면 1 큰수를 함수의 파라미터로 다시 입력
    while True:
        if isPrime(i):
            print(i)
            break
        i += 1