"""
https://www.acmicpc.net/problem/2696
2696.중앙값 구하기
골드2
풀이2.84ms
"""
import sys
import heapq

input = sys.stdin.readline
for _ in range(int(input())):
    N = int(input())
    nums = []
    for _ in range(N // 10 + 1):
        nums += list(map(int, input().split()))
    medians = [nums[0]]
    left = [-nums[0]]
    right = []

    for i in range(1, N):
        if i % 2 == 0:
            heapq.heappush(left, -nums[i])
            heapq.heappush(right, -heapq.heappop(left))
            medians.append(-left[0])
        else:
            heapq.heappush(right, nums[i])
            heapq.heappush(left, -heapq.heappop(right))


    print(len(medians))
    for i in range(len(medians) // 10 + 1):
        print(*medians[i * 10: i * 10 + 10])
