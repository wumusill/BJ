import sys


# 맨 뒤 글자를 제거해주는 함수
def deleteA(string : str):
    return string[:-1]


# 맨 뒤 글자를 제거하고 문자열을 뒤집는 함수
def reverseB(string : str):
    return string[:-1][::-1]


a = sys.stdin.readline().strip()
b = sys.stdin.readline().strip()

# a와 b가 같으면 반복문 탈출
while a != b:
    # b 문자열이 다 제거되었다면 변경이 불가능한 경우
    if len(b) == 0:
        print(0)
        break
    # 맨 뒤 글자가 'A'면 함수 실행
    if b[-1] == 'A':
        b = deleteA(b)
    # 맨 뒤 글자가 'B'면 함수 실행
    elif b[-1] == 'B':
        b = reverseB(b)
    # 맨 뒤 글자가 'A', 'B' 둘 다 아니면 변경이 불가능한 경우
    else:
        print(0)
        break

# break 없이 반복문을 완수하면 a에서 b로 변경이 가능한 경우
else:
    print(1)