"""
https://www.acmicpc.net/problem/11047
11047.동전 0
실버4
풀이2.68ms
"""
import sys

input = sys.stdin.readline
N, K = map(int, input().split())
coins = [int(input()) for _ in range(N)]
coins.sort(reverse=True)
answer = 0

for coin in coins:
    quotient = K // coin
    K -= coin * quotient
    answer += quotient

print(answer)