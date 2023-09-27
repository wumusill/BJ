# 틀림
import sys

alphabet = {'A': [-1, 0], 'B': [-1, 0], 'C': [-1, 0], 'D': [-1, 0], 'E': [-1, 0], 'F': [-1, 0], 'G': [-1, 0],
            'H': [-1, 0], 'I': [-1, 0], 'J': [-1, 0], 'K': [-1, 0], 'L': [-1, 0], 'M': [-1, 0], 'N': [-1, 0],
            'O': [-1, 0], 'P': [-1, 0], 'Q': [-1, 0], 'R': [-1, 0], 'S': [-1, 0], 'T': [-1, 0], 'U': [-1, 0],
            'V': [-1, 0], 'W': [-1, 0], 'X': [-1, 0], 'Y': [-1, 0], 'Z': [-1, 0]}

words = []
n = int(sys.stdin.readline())
for _ in range(n):
    word = list(sys.stdin.readline().strip())
    words.append(word)

words.sort(key=lambda x: len(x), reverse=True)

for word in words:
    for i in range(len(word)):
        key = word[i]
        alphabet[key][0] = max(len(word) - i, alphabet[key][0])
        alphabet[key][1] += 1

temp_alphabet = sorted(alphabet.items(), key=lambda x: (x[1][0], x[1][1]), reverse=True)

num = 9
for key, val in temp_alphabet:
    if val != -1:
        alphabet[key] = str(num)
        num -= 1

ans = []
for word in words:
    l = list(map(lambda x: alphabet[x], word))
    num = int(''.join(l))
    ans.append(num)

print(sum(ans))
####################################################################################################################
import sys

alphabet = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0, 'M': 0,
            'N': 0, 'O': 0, 'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'U': 0, 'V': 0, 'W': 0, 'X': 0, 'Y': 0, 'Z': 0}

words = []
n = int(sys.stdin.readline())
for _ in range(n):
    word = list(sys.stdin.readline().strip())
    words.append(word)

for word in words:
    for i in range(len(word)):
        num = 10 ** (len(word) - i - 1)
        alphabet[word[i]] += num

alphabet = sorted(alphabet.items(), key=lambda x: x[1], reverse=True)

ans = 0
num = 9
for key, val in alphabet:
    if val > 0:
        ans += val * num
        num -= 1

print(ans)

# 5
# AB
# BC
# CD
# DE
# EF
# 384

# 4
# ABCD
# BCDA
# CDAB
# DABG
# 33329

# 3
# Z
# B
# A
# 24

# 3
# AAAAA
# BBBDD
# CCA
# 189644

# 6
# ABABABAB
# BABABABA
# ABABABAB
# BABABABA
# CCCCCCCA
# CCCCCCBA
# 533333350