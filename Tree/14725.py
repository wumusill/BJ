import sys


def add(dictionary, words):
    for word in words:                          # 단어 순회
        if word not in dictionary:              # 사전에 없는 단어라면
            dictionary[word] = {}               # 사전에 단어 추가 후 다음 단어가 들어갈 dictionary를 value로 생성
        dictionary = dictionary[word]           # 사전 갱신하고 다음 단어 탐색


def print_tree(tree, length):
    for key in sorted(tree.keys()):             # key 정렬
        print("--" * length + key)              # 단어 출력
        print_tree(tree[key], length + 1)       # 자식 단어 출력하기 위한 재귀


n = int(sys.stdin.readline())
head = {}
for _ in range(n):
    l = sys.stdin.readline().rstrip().split()
    words = l[1:]
    add(head, words)

print_tree(head, 0)