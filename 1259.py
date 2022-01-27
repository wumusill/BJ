def palindrome(word):
    for i in range(len(word)//2):
        if word[i] != word[len(word)-i-1]:
            return 'no'
        else:
            continue
    return 'yes'

while True:
    word = input()
    if word == '0':
        break
    print(palindrome(word))