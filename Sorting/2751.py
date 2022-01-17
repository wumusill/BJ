import sys

n = int(sys.stdin.readline())
num_list = [int(sys.stdin.readline()) for _ in range(n)]

# # 메모리 초과
# def quick_sort_2(array):
#     if len(array) <= 1:
#         return array
#
#     pivot = array[0]
#     tail = array[1:]
#
#     left_side = [x for x in tail if x <= pivot]
#     right_side = [x for x in tail if x > pivot]
#
#     return quick_sort_2(left_side) + [pivot] + quick_sort_2(right_side)
#
# for i in quick_sort_2(array):
#     print(i)
#
# # 시간 초과
# def quick_sort(array, start, end):
#     if start >= end:
#         return
#     pivot = start
#     left = start + 1
#     right = end
#
#     while left <= right:
#         while left <= end and array[left] <= array[pivot]:
#             left += 1
#         while right > start and array[right] >= array[pivot]:
#             right -= 1
#         if left > right:
#             array[right], array[pivot] = array[pivot], array[right]
#         else:
#             array[left], array[right] = array[right], array[left]
#     quick_sort(array, start, right - 1)
#     quick_sort(array, right + 1, end)
#
#
# quick_sort(num_list, 0, len(num_list) - 1)
# for i in num_list:
#     print(i)

#############################################################################

for i in sorted(num_list):
    print(i)