import sys


def solution(word):
    left, right = 0, len(word) - 1                              # 포인터 설정
    chance = True                                               # 단어 하나를 제거할 수 있는 기회
    while left < right:                                         # 단어 순회
        if word[left] == word[right]:                           # 포인터가 가리키는 알파벳이 같으면 다음 포인터 확인
            left += 1
            right -= 1
        else:                                                   # 포인터가 가리키는 알파벳이 다르면
            if chance:                                          # 하나를 제거할 수 있는 기회가 남았는지 확인

                if word[left + 1] == word[right]:               # 왼쪽 글자를 제거했을 때
                    temp_word = word[left + 1:right + 1]        # 제거 후 뒤집어도 똑같은지 확인
                    if temp_word == temp_word[::-1]:            # 똑같으면 유사 회문
                        return 1

                if word[left] == word[right - 1]:               # 오른쪽 글자를 제거했을 때
                    temp_word = word[left:right]
                    if temp_word == temp_word[::-1]:
                        return 1

                chance = False                                  # 기회 없음 처리

            else:                                               # 기회가 없으면 회문과 유사 회문 둘 다 아님
                return 2

    return 0                                                    # 반복문을 무사히 마쳤으면 회문


n = int(sys.stdin.readline())
for _ in range(n):
    word = sys.stdin.readline().rstrip()
    print(solution(word))
#######################################################################################################################
# 위 코드로 패스했지만 다시 보니 chance가 무의미함
# 그래서 chance를 활용하지 않는 아래 코드를 제출해보니 시간 초과
# 무슨 차이인지 모르는 중
import sys


def solution(word):
    left, right = 0, len(word) - 1
    while left < right:
        if word[left] == word[right]:
            left += 1
            right -= 1
        else:
            if word[left + 1] == word[right]:
                temp_word = word[left + 1:right + 1]
                if temp_word == temp_word[::-1]:
                    return 1

            if word[left] == word[right - 1]:
                temp_word = word[left:right]
                if temp_word == temp_word[::-1]:
                    return 1

            else:
                return 2

    return 0


n = int(sys.stdin.readline())
for _ in range(n):
    word = sys.stdin.readline().rstrip()
    print(solution(word))
#######################################################################################################################
# 아래 코드가 위 chance의 의도를 더 명확하게 활용하는 것 같음
# 함수 두 개로 더 깔끔하고 가독성도 좋은 코드 같음
import sys


def chance(word, left, right):                                  # 유사 회문인지 (회문, 유사 회문) 둘 다 아닌지 판단
    while left < right:
        if word[left] == word[right]:
            left += 1
            right -= 1
        else:
            return False

    return True


def solution(word, left, right):                                # 회문인지 아닌지 판단
    while left < right:
        if word[left] == word[right]:
            left += 1
            right -= 1
        else:                                                   # 알파벳이 다르면 유사 회문인지 그마저도 아닌지 판단
            check_left = chance(word, left + 1, right)          # 왼쪽 알파벳 제거
            check_right = chance(word, left, right - 1)         # 오른쪽 알파벳 제거

            if check_left or check_right:                       # 둘 중 하나를 제거했을 때 회문이라면 유사 회문
                return 1
            else:
                return 2

    return 0                                                    # 반복문 무사 통과했으면 회문


n = int(sys.stdin.readline())
for i in range(n):
    word = sys.stdin.readline().rstrip()
    print(solution(word, 0, len(word) - 1))


# 4
# xyyyyxy
# yxyyyyx
# abca
# acba
# 1
# 1
# 1
# 1