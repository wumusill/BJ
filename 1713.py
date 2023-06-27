import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
l = list(map(int, sys.stdin.readline().strip().split()))
d = dict()

# 피추천인 1명씩 순회
for i in l:
    # 만약 후보자 자리가 다 찼다면
    if len(d) == n and i not in d:
        # 후보자와 추천 수를 등록 순서대로 순회
        for key, val in d.items():
            # 가장 먼저 등록된 후보자 중 추천 수가 가장 낮은 후보자를 만나면
            if val == min(d.values()):
                # 후보자를 제외하고
                del d[key]
                # 새로운 피추천인을 후보자로 등록
                d[i] = 1
                break
        continue

    # 후보자에 자리가 있다면 피추천인 추가
    if i not in d:
        d[i] = 1
    else:
        d[i] += 1

print(*sorted(d.keys()))