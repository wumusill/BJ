import sys

# {민식어 : 영어} 형태로 저장
# 영어(value) 기준 정렬
# 키 하나씩 출력
# 그전에 'ng'는 하나의 원소(z)로써 치환해주는 작업 필요
convert_dict = {'a': 'A', 'b': 'B', 'k': 'C', 'd': 'D', 'e': 'E', 'g': 'F', 'h': 'G', 'i': 'H', 'l': 'I', 'm': 'J',
                'n': 'K', 'z': 'L', 'o': 'M', 'p': 'N', 'r': 'O', 's': 'P', 't': 'Q', 'u': 'R', 'w': 'S', 'y': 'T'}

n = int(sys.stdin.readline())
words = {}
for _ in range(n):
    key = sys.stdin.readline().strip()
    # 'ng'를 안쓰이는 알파벳 중 하나인 'z'로 변환, 출력은 입력 받은 그대로 돼야 하므로 key를 덮어쓰지 않음
    convert_key = key.replace('ng', 'z')

    # 알파벳 하나하나하 민식어로 치환하는 반복문
    letters = list(convert_key)
    value = ''
    for letter in letters:
        value += convert_dict[letter]

    # {민식어 : 영어} 저장
    words[key] = value

# 영어를 기준으로 items 정렬
words = sorted(words.items(), key=lambda x: x[1])

# 정렬된 items 중 민식어인 key만 출력
for word in words:
    print(word[0])