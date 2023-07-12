import sys

cnt = 1
while True:
    l = list(sys.stdin.readline().strip())
    ans = 0
    stack = []

    # 입력 종료 조건
    if '-' in l:
        break
    # 입력값 순회
    for letter in l:
        # 스택이 비어있다면 무조건 스택에 추가
        if not stack:
            # } 문자의 경우 무조건 회전 연산을 해야하므로 ans += 1
            if letter == "}":
                ans += 1
            stack.append(letter)
        # 스택이 비어있지 않다면
        else:
            # } 문자의 경우 스택 pop
            if letter == '}':
                stack.pop()
            # { 문자의 경우 스택에 추가
            else:
                stack.append(letter)

    # 스택에는 ['{', '{'] 나 ['}', '{'] 의 경우만 남게 됨
    # 위 같은 경우 스택에 남아있는 원소들의 개수를 2로 나누어 주면 안정적인 문자열이 되기 위해 필요한 연산 수를 알 수 있음
    ans += len(stack) // 2

    print(f"{cnt}. {ans}")
    cnt += 1

# }{
# {}{}{}
# {{{}
# {{}}
# }}}{
# }}{{
# }}}}}}
# }{}{
# }}{}
# --


# 2
# 0
# 1
# 0
# 3
# 2
# 3
# 2
# 1