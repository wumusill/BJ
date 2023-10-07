import sys

n, m = map(int, sys.stdin.readline().split())

# 문자 사전순 정렬
letters = sorted(sys.stdin.readline().strip().split())
ans = []


def solution(password, letters, mo, ja):
    # 비밀번호의 조건 : 모음 1개 이상, 자음 2개 이상을 가진 n자리 수 문자
    if len(password) == n and mo > 0 and ja > 1:
        ans.append(''.join(password))
    for i in range(len(letters)):
        letter = letters[i]

        # 현재 문자 추가 후 비밀번호 자모음 개수 갱신
        password.append(letter)
        if letter in ['a', 'e', 'i', 'o', 'u']:
            mo += 1
        else:
            ja += 1

        # 현재 문자 추가 후 남은 문자 대상으로 백트래킹
        solution(password, letters[i + 1:], mo, ja)

        # 추가돤 문자 제거 후 비밀번호 자모음 개수 갱신 -> 다음 문자 순회
        password.pop()
        if letter in ['a', 'e', 'i', 'o', 'u']:
            mo -= 1
        else:
            ja -= 1


solution([], letters, 0, 0)

for answer in ans:
    print(answer)