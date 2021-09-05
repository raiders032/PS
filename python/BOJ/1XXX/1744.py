"""
https://www.acmicpc.net/problem/1744
1744.수 묶기
골드4
풀이2.88ms
"""
import sys
import heapq

input = sys.stdin.readline
positive_nums = list()
negative_nums = list()
answer = 0

for _ in range(int(input())):
    num = int(input())
    if num > 0:
        heapq.heappush(positive_nums, -num)
    else:
        heapq.heappush(negative_nums, num)

while positive_nums:
    num1 = -heapq.heappop(positive_nums)

    if positive_nums:
        num2 = -heapq.heappop(positive_nums)
        answer += num1 * num2 if num2 != 1 else num1 + num2
    else:
        answer += num1

while negative_nums:
    num1 = heapq.heappop(negative_nums)

    if negative_nums:
        num2 = heapq.heappop(negative_nums)
        answer += num1 * num2
    else:
        answer += num1

print(answer)