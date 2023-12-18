import sys

n = int(sys.stdin.readline())
k = int(sys.stdin.readline())
l = sorted(map(int, sys.stdin.readline().split()))

# 기지국이 센서의 수보다 같거나 크다면 연산 무의미
if n <= k:
    print(0)
else:
    # 차이가 가장 긴 순서로 정렬
    # 긴 것 사이에 기지국 추가
    diff = []
    for i in range(1, n):
        diff.append(l[i] - l[i - 1])

    # 거리 오름차순 정렬
    diff.sort()

    # k개의 집중국을 세우려면 (k - 1)번 나누면 됨
    # 거리가 가장 먼 순서대로 분리
    for _ in range(k - 1):
        diff.pop()

    # 각 집중국이 커버하는 최댓값과 최솟값의 차이는 연속된 차이의 합과 같음
    print(sum(diff))