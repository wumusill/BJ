# 점프 가능 횟수가 0이면서 해당 정답 자리가 빈자리(0)일 때 해당 번호가 들어갈 수 있는 자리

# 점프 가능 횟수(l) 순회, 횟수만큼 왼쪽에 큰 수가 있어야 함
# 작은 수 부터 순회

# 빈자리(0)이면 큰수가 들어와야 하는 자리이므로 개수 차감하고 점프
# 0이 아니면 이미 들어간 수가 있기 때문에 개수 차감 없이 점프
# 개수가 0일때 빈자리(0)를 만나면 대입
import sys

n = int(sys.stdin.readline())

# 수 (idx + 1)가 점프할 수 있는 횟수를 기록된 리스트
l = list(map(int, sys.stdin.readline().split()))
ans = [0] * n

# 작은 번호부터 시작
num = 1

# 점프 가능 횟수 순회
for cnt in l:
    # index 초기화
    idx = 0
    # ans index 순회
    for j in range(n):
        # 빈자리면서 점프 가능 횟수가 없으면 그 자리 숫자 대입
        if cnt == 0 and ans[idx] == 0:
            ans[idx] = num
            break
        # 빈자리(0)이면 점프 횟수 차감
        if ans[j] == 0:
            cnt -= 1
        # 다음 자리 확인
        idx += 1
    # 다음 숫자 확인
    num += 1

print(*ans)