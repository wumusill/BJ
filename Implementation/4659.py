import sys

while True:
    word = sys.stdin.readline().rstrip()
    if word == 'end':
        break

    # 모음이 있는지 판단
    for i in ['a', 'e', 'i', 'o', 'u']:
        if i in word:
            break
    else:
        print(f"<{word}> is not acceptable.")
        continue

    # 모음 or 자음이 3개 연속인지 판단
    second = True
    word_bool = list(map(lambda x: True if x in ['a', 'e', 'i', 'o', 'u'] else False, list(word)))
    for i in range(2, len(word_bool)):
        a, b, c = word_bool[i - 2], word_bool[i - 1], word_bool[i]
        if (a and b and c) or (not a and not b and not c):
            second = False
            break

    # 두 번째 조건 통과하는 애들만 다음 조건 검토
    if not second:
        print(f"<{word}> is not acceptable.")
        continue
    else:
        # 'ee', 'oo'를 제외하고 같은 글자가 연속적으로 두번 오는지 판단
        third = True
        for i in range(1, len(word)):
            if word[i] == 'e' or word[i] == 'o':            # 'e', 'o'는 고려 대상 아님
                continue
            elif word[i - 1] == word[i]:                    # 'e', 'o' 제외 같은 글자면 break
                third = False
                break

        if not third:
            print(f"<{word}> is not acceptable.")
        else:
            print(f"<{word}> is acceptable.")