import sys


def solution(dictionary, word):
    result = ''
    condition = True                                    # 단어가 이미 출력됐는지 아닌지 판단하기 위한 bool

    for letter in word:                                 # 한 글자씩 순회
        result += letter                                # 지금까지 순회한 글자들

        if letter not in dictionary:                    # 현재 탐색 중인 글자가 처음 등장했다면
            dictionary[letter] = {}                     # 글자 기록하고 트리 확장

            if condition:                               # 트리를 확장했는데 단어가 출력되지 않았다면 -> 가장 짧은 별칭
                print(result)                           # 출력
                condition = False                       # 다음 글자 탐색할 때 출력되지 않도록 처리

        dictionary = dictionary[letter]                 # 자식 노드로 이동

    if result in nickname_dict:                         # 풀 닉네임이 이미 사전에 존재한다면
        nickname_dict[result] += 1                      # 등장 횟수 갱신
        result += str(nickname_dict[result])            # 순회한 글자에 번호 추가
    else:                                               # 풀 닉네임이 사전에 존재하지 않으면 추가
        nickname_dict[result] = 1

    if condition:                                       # 단어가 출력된 적이 없을 때 출력
        print(result)


n = int(sys.stdin.readline())
nickname_dict = {}                                      # 닉네임 기록할 dictionary
head = {}                                               # Trie 수행할 dictionary
for _ in range(n):
    nickname = list(sys.stdin.readline().rstrip())
    solution(head, nickname)