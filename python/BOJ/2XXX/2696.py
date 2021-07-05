"""
https://www.acmicpc.net/problem/2696
2696.중앙값 구하기
골드2
풀이1.96ms
"""
import sys
import heapq

input = sys.stdin.readline
T = int(input())
for _ in range(T):
    M = int(input())
    nums = []
    for _ in range(M // 10 + 1):
        nums = nums + list(map(int, input().split()))
    medians = [nums[0]]
    left = [-nums[0]]
    right = []
    for i in range(1, M):
        if i % 2 == 0:
            if nums[i] <= -left[0]:
                heapq.heappush(left, -nums[i])
            else:
                heapq.heappush(right, nums[i])
                heapq.heappush(left, -heapq.heappop(right))
            medians.append(-left[0])
        else:
            if -left[0] <= nums[i]:
                heapq.heappush(right, nums[i])
            else:
                heapq.heappush(left, -nums[i])
                heapq.heappush(right, -heapq.heappop(left))
    print(len(medians))
    for i in range(len(medians) // 10 + 1):
        print(*medians[i * 10:i * 10 + 10])
