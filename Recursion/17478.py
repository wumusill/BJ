n = int(input())

print("어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.")


def wiarf(t):
    _str = "____"
    sentence_1 = _str * t + "\"재귀함수가 뭔가요?\""
    sentence_2 = _str * t + "\"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어."
    sentence_3 = _str * t + "마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지."
    sentence_4 = _str * t + "그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어.\""
    sentence_5 = _str * t + "\"재귀함수는 자기 자신을 호출하는 함수라네\""
    sentence_6 = _str * t + "라고 답변하였지."

    if t == n:
        print(sentence_1)
        print(sentence_5)
        print(sentence_6)
        return

    print(sentence_1)
    print(sentence_2)
    print(sentence_3)
    print(sentence_4)

    wiarf(t + 1)

    print(sentence_6)
    return


wiarf(0)