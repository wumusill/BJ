from collections import deque

stack = deque()
dict = {'(':')', '[':']'}

while True:
    sentence = input()
    if sentence == '.':
        break

    breaker = True

    for spell in sentence:
        if spell in dict.keys():
            stack.append(spell)

        elif spell in dict.values():
            if stack:
                if spell == dict[stack.pop()]:
                    continue
            breaker = False
            break

    if breaker and not stack:
        print('yes')
    else:
        print('no')
#############################################################################
# 위는 틀림 아래가 맞음

brackets = {'(': ')', '[': ']'}

while True:
    stack = []
    check = True
    _str = input()
    if _str == ".":
        break

    for char in _str:
        if char in brackets.keys():
            stack.append(char)

        elif char in brackets.values():
            if stack:
                if char == brackets[stack.pop()]:
                    continue

            check = False
            break

    if check and not stack:
        print("yes")
    else:
        print("no")