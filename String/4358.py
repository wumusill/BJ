# 맞은 코드
# .f 사용
import sys

trees = {}
cnt = 0
while True:
    tree = sys.stdin.readline().strip()
    if not tree:
        break
    if tree not in trees:
        trees[tree] = 1
    else:
        trees[tree] += 1
    cnt += 1

sorted_trees = sorted(trees.items(), key=lambda x: x[0])
ans_key = list(map(lambda x: x[0], sorted_trees))
ans_val = list(map(lambda x: x[1] / cnt * 100, sorted_trees))

for key, val in zip(ans_key, ans_val):
    print(f"{key} {val:.4f}")
#################################################################
# 틀린 코드
# round 사용 : round 작동 방식에 한계점 있음
# https://docs.python.org/ko/3/library/functions.html?highlight=round#round
import sys

trees = {}
cnt = 0
while True:
    tree = sys.stdin.readline().strip()
    if not tree:
        break
    if tree not in trees:
        trees[tree] = 1
    else:
        trees[tree] += 1
    cnt += 1

sorted_trees = sorted(trees.items(), key=lambda x: x[0])
ans_key = list(map(lambda x: x[0], sorted_trees))
ans_val = list(map(lambda x: round(x / cnt * 100, 4), sorted_trees))

for ans in zip(ans_key, ans_val):
    print(*ans)