# 시간 초과
import sys


def is_palindrome(word):
    for i in range(len(word) // 2):
        if word[i] != word[len(word) - i - 1]:
            return False
    return True


def solution1(word):
    answer = -1
    if not word:                                        # 단어가 공백이면 -1 반환
        return answer

    if not is_palindrome(word):                         # 단어가 회문이 아니면 단어의 길이 반환
        return len(word)
    else:
        left = solution1(word[1:])                      # 왼쪽 문자 하나를 제거한 단어에 대해 재귀 수행
        right = solution1(word[:-1])                    # 오른쪽 문자 하나를 제거한 단어에 대해 재귀 수행
        answer = max(answer, left, right)               # 최댓값 갱신

    return answer


word = sys.stdin.readline().rstrip()
print(solution1(word))
#######################################################################################################################
# 주어진 문자가 회문이 아니라면 문자열의 길이가 정답
# 회문이라면 두 가지 경우 확인
    # 1. 'ABCBA' 같이 두 개 이상의 문자로 이루어진 회문
    # 2. 'ZZZ' 같이 하나의 문자로 이루어진 회문
# 1번 경우의 회문이라면 (문자열 길이 - 1)가 정답
# 2번 경우의 회문이라면 무조건 -1

import sys


def is_palindrome(word):
    for i in range(len(word) // 2):
        if word[i] != word[len(word) - i - 1]:
            return False
    return True


def solution(word):
    if is_palindrome(word):
        if len(set(list(word))) == 1:
            return -1
        else:
            return len(word) - 1
    else:
        return len(word)


word = sys.stdin.readline().rstrip()
print(solution(word))

# ABCBACBCA
# 9