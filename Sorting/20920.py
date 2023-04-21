import sys

n, m = map(int, sys.stdin.readline().split())

# 단어를 기록할 단어장
vocab = {}
for _ in range(n):
    # 입력 받은 단어
    word = sys.stdin.readline().rstrip()
    # 단어의 길이가 m 이상인 것만 단어장에 기록
    if len(word) >= m:
        # 이미 기록되어 있으면 횟수 + 1
        if word in vocab:
            vocab[word] += 1
        # 처음 등장했다면 새로 기록
        else:
            vocab[word] = 1

# 단어 정렬 : 등장 횟수 DESC, 단어 길이 DESC, 단어 사전순 ASC
vocab = sorted(vocab.items(), key=lambda item: (-item[1], -len(item[0]), item[0]))

# 정렬된 단어 순서대로 출력
for item in vocab:
    print(item[0])