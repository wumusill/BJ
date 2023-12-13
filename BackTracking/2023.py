import sys

n = int(sys.stdin.readline())
answer = []


# 소수 판별기
def isprime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


# 신기한 소수 찾기
def solution(n, num):
    if len(num) == n:                   # 재귀 종료 조건 : 숫자의 길이가 n이랑 같으면 탐색 종료
        if isprime(int(num)):           # n자리의 소수라면 정답에 기록
            answer.append(int(num))
        return

    for i in range(10):                 # 1 ~ 9의 숫자를 뒤에 추가
        new = num + str(i)
        if isprime(int(new)):           # 새로운 숫자가 소수라면 재귀 진행
            solution(n, new)


# 1 ~ 9까지 소수면 함수 실행
for i in range(1, 10):
    if isprime(i):
        solution(n, str(i))

for ans in answer:
    print(ans)