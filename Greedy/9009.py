import sys


# 피보나치 수열의 원소가 n보다 커질 때까지 구한 뒤 리스트로 반환하는 함수
def fibo(n):
    l = [0, 1]
    res = 1
    while res < n:
        res = l[-1] + l[-2]
        l.append(res)
    return l


t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())

    # 피보나치 수열 구함
    fibo_list = fibo(n)

    # 정답의 원소들을 저장할 리스트(내림차순)
    ans_list = []

    # n이 0이 될 때까지 반복
    while n != 0:
        # 수열의 가장 마지막 원소
        res = fibo_list.pop()
        # 만약 원소가 더 작다면 정답 리스트에 기록하고 n에서 빼기
        if n >= res:
            n -= res
            ans_list.append(res)

    # 정답은 오름차순으로 출력해야 하므로 뒤에서 하나씩 출력
    while ans_list:
        ans = ans_list.pop()
        print(ans, end=' ')
