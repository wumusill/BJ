import sys

n = int(sys.stdin.readline())

# 알파벳 개수만큼 연결을 기록할 matrix
dist = [[False for _ in range(ord('z') - ord('a') + 1)] for _ in range(ord('z') - ord('a') + 1)]

for _ in range(n):
    a, b = sys.stdin.readline().strip().split(' is ')

    # 알파벳이 몇 번째인지 순서로 변환
    a = ord(a) - ord('a')
    b = ord(b) - ord('a')
    dist[a][b] = True

# 플로이드 워셜 연산
for k in range(ord('z') - ord('a') + 1):
    for a in range(ord('z') - ord('a') + 1):
        for b in range(ord('z') - ord('a') + 1):
            if dist[a][k] and dist[k][b]:
                dist[a][b] = True

m = int(sys.stdin.readline())

for _ in range(m):
    a, b = sys.stdin.readline().strip().split(' is ')
    a = ord(a) - ord('a')
    b = ord(b) - ord('a')

    if dist[a][b]:
        print('T')
    else:
        print('F')