# https://aerocode.net/392 설명이 잘 된 블로그
import sys

n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
nums.sort()

answer = 1

for i in range(n):
    if nums[i] > answer:
        break

    answer += nums[i]

print(answer)