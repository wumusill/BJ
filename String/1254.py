# 앞에서부터 한 글자씩 제외하면서 펠린드롬인지 확인
# 만약 펠린드롬이라면 뒤에 단어를 더 추가하지 않고 종료
# 아니라면 뒤에 맨 앞글자를 맨 뒤에 추가해야 하므로 정답 단어의 길이 += 2
import sys

# 입력 받은 단어가 팰린드롬인지 아닌지 판단해주는 함수
def is_pal(word):
    for i in range(len(word) // 2):
        if word[i] != word[len(word) - i - 1]:
            return False
    return True


_input = sys.stdin.readline().strip()
ans = 0
for i in range(len(_input)):
    # 단어 전체가 펠린드롬인지 확인하고 앞에서부터 한 글자씩 제거 후 재확인
    word = _input[i:]
    if not is_pal(word):
        ans += 2
    else:
        ans += len(word)
        break

print(ans)