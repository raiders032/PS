"""
https://www.acmicpc.net/problem/1715
1715.카드 정렬하기
골드4
풀이1.228ms
"""
import sys, heapq

input = sys.stdin.readline

N = int(input())
cards = []
ans = 0
for _ in range(N):
    heapq.heappush(cards, int(input()))

while len(cards) > 1:
    count = heapq.heappop(cards) + heapq.heappop(cards)
    ans += count
    heapq.heappush(cards, count)

print(ans)
