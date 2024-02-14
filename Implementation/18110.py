# round 활용 시 주의할 점
# 4사5입 : 4 이하면 버리고 5 이상이면 올림
# 하지만 만약 대부분의 데이터가 5로 끝난다면 전체적으로 0.5정도 커짐
# 이런 통계적 오류를 막기 위해 고안된 방법이 5사5입
# 5사5입에는 여러 방법이 있으나, Python의 round 함수는 반올림 자리가 5인 경우, 앞 자리가 홀수면 올림, 짝수면 버림

# print(round(2.5))     = 2
# print(round(3.5))     = 4
# print(new_round(2.5)) = 3
import sys


def new_round(num):                                             # 사사오입을 위해 구현된 함수
    return int(num) + (1 if num - int(num) >= 0.5 else 0)       # 소수 부분이 0.5 이상이면 자연수에 1을 더하고 아니면 0을 더함


def solution(n, score):
    score.sort()                                                # 점수 정렬
    idx = new_round(n * 0.15)                                   # 상위 15%, 하위 15% 제거 위한 기준점 계산
    element = score[idx:n - idx]                                # 기준점을 넘는 이상치들 제거
    mean = sum(element) / len(element)                          # 이상치 제거된 요소들의 평균 계산
    answer = new_round(mean)                                    # 계산된 평균 사사오입
    print(answer)


n = int(sys.stdin.readline())
if n == 0:
    print(0)
else:
    score = [int(sys.stdin.readline()) for _ in range(n)]
    solution(n, score)