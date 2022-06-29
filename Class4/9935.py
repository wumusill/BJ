# 시간초과
# import sys
#
# word = sys.stdin.readline().strip()
# bomb = sys.stdin.readline().strip()
#
# while True:
#     new_word = word.replace(bomb, '')
#
#     if len(new_word) == 0:
#         print("FRULA")
#         break
#     if new_word == word:
#         print(word)
#         break
#     else:
#         word = new_word
################################################################################
import sys

word_list = list(sys.stdin.readline().strip())
bomb = list(sys.stdin.readline().strip())
length = len(bomb)

stack = []
for spell in word_list:
    stack.append(spell)
    if spell == bomb[-1]:
        last_word = stack[-length:]
        if last_word == bomb:
            for _ in range(length):
                stack.pop()

if not stack:
    print('FRULA')
else:
    print(''.join(stack))