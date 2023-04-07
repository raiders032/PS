"""
https://www.acmicpc.net/problem/11508
11508.2+1 세일
실버4
풀이1.76ms
"""
import sys
input = sys.stdin.readline

N = int(input())
prices = [int(input()) for _ in range(N)]
prices.sort(reverse=True)
sheep_count = 0
for i in range(len(prices)):
    if i % 3 == 2:
        continue
    sheep_count += prices[i]
print(sheep_count)