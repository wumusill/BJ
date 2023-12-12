import sys

n = int(sys.stdin.readline())

# 들어간 순서
enter = {sys.stdin.readline().rstrip() : i for i in range(n)}

# 나온 순서
exit = [enter[sys.stdin.readline().rstrip()] for _ in range(n)]

ans = 0

for i in range(n):                  # 하나씩 순회
    for j in range(i + 1, n):       # index 뒤 순회
        if exit[i] > exit[j]:       # 만약 뒤에 하나라도 터널에 일찍 들어간 차량(숫자가 작은 차량)이 있다면 i는 추월 차량
            ans += 1
            break

print(ans)