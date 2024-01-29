import sys
import heapq


def solution(l):
    '''
    right_heap : 최대힙으로 리스트에서 중앙값보다 작은 값들이 들어갈 힙
    left_heap : 최소힙으로 리스트에서 중앙값보다 큰 값들이 들어갈 힙

    두 힙의 길이가 같다면 무조건 right_heap에 원소 추가
    right_heap에 원소를 추가했을 때 == 원소의 개수가 홀수일 때 == 하나의 중앙값이 발생할 때

    만약 left_heap의 최솟값(중앙값보다 큰 값들 중 최솟값)이 right_heap의 최댓값(중앙값보다 작은 값들 중 최댓값)보다 크다면, 두 값을 switch
    중앙값보다 작은 값 중 가장 큰 값이 중앙값이 되므로, right_heap의 첫 원소가 중앙값이 됨
    '''
    median, left_heap, right_heap = [], [], []                      # 중앙값 기록할 리스트와 힙 두 개 선언
    for num in l:
        if len(left_heap) == len(right_heap):                       # 두 힙의 길이가 같으면 right_heap에 원소 추가
            heapq.heappush(right_heap, (-num, num))

            if left_heap and right_heap:                            # left_heap의 최솟값과 right_heap의 최댓값 비교
                if left_heap[0] < right_heap[0][1]:                 # left_heap의 최솟값이 더 작으면, 두 값을 switch
                    left = heapq.heappop(left_heap)
                    right = heapq.heappop(right_heap)[1]
                    heapq.heappush(left_heap, right)
                    heapq.heappush(right_heap, (-left, left))

            median.append(right_heap[0][1])                         # 중앙값(right_heap의 최댓값) 리스트에 기록

        else:                                                       # 두 힙의 길이가 다르면 left_heap에 원소 추가
            heapq.heappush(left_heap, num)

    return median


t = int(sys.stdin.readline())
for _ in range(t):
    m = int(sys.stdin.readline())
    if m < 11:                                                      # 수열의 원소가 10개씩 주어짐
        l = list(map(int, sys.stdin.readline().split()))            # 10개 이하면 수열 1번 입력 받음
    else:
        l = []                                                      # 원소가 11개 이상이면
        for _ in range(m // 10):
            l += list(map(int, sys.stdin.readline().split()))       # 10개씩 먼저 받고
        if m % 10 != 0:
            l += list(map(int, sys.stdin.readline().split()))       # 나머지를 추가로 받음

    median = solution(l)                                            # 입력 받은 수열로 함수 실행

    print(len(median))                                              # 결과물 출력, 중앙값은 10개씩 출력
    for i in range(0, len(median), 10):
        print(*median[i:i + 10])