"""
https://www.acmicpc.net/problem/1744
1744.수 묶기
골드4
풀이1.84ms
"""
import sys
import heapq

input = sys.stdin.readline
N = int(input())
nums = [int(input()) for _ in range(N)]
positive_nums = list()
negative_nums = list()
ans = 0

for num in nums:
    if num > 0:
        heapq.heappush(positive_nums, -num)
    else:
        heapq.heappush(negative_nums, num)

while positive_nums:
    num1 = -heapq.heappop(positive_nums)

    if positive_nums:
        num2 = -heapq.heappop(positive_nums)
        ans += num1 * num2 if num2 != 1 else num1 + num2
    else:
        ans += num1

while negative_nums:
    num1 = heapq.heappop(negative_nums)
    num2 = 1

    if negative_nums:
        num2 = heapq.heappop(negative_nums)

    ans += num1 * num2

print(ans)