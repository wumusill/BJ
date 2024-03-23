import sys


def add(dictionary, words):
    for word in words:
        if word not in dictionary:
            dictionary[word] = {}
        dictionary = dictionary[word]


def print_tree(tree, length):
    for key in sorted(tree.keys()):
        print(" " * length + key)
        print_tree(tree[key], length + 1)


n = int(sys.stdin.readline())
head = {}
for _ in range(n):
    directory = (list(sys.stdin.readline().rstrip().split('\\')))
    add(head, directory)

print_tree(head, 0)