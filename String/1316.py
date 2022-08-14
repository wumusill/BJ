n = int(input())
str_list = [input() for _ in range(n)]
result = 0

for word in str_list:
    already =[]
    length = 0
    for i in range(len(word)):
        if len(already) == 0:
            length += 1
            already.append(word[i])
        else:
            if word[i] == already[-1]:
                length += 1
                continue
            if word[i] not in already:
                length += 1
                already.append(word[i])
            else:
                break
    if length == len(word):
        result += 1

print(result)
#############################################################################
n = int(input())
answer = 0

for _ in range(n):
    word = input()
    already = []
    flag = True
    for i in range(len(word)):
        if word[i] not in already:
            already.append(word[i])
        else:
            if word[i] == word[i - 1]:
                continue
            else:
                flag = False
                break
    if flag:
        answer += 1

print(answer)