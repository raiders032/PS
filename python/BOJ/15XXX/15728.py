"""
https://www.acmicpc.net/problem/15728
15728.에리 - 카드
풀이1.84ms
"""
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
cards1 = list(map(int, input().split()))
cards2 = list(map(int, input().split()))
max_score = [-sys.maxsize] * N

for index, number2 in enumerate(cards2):
    for number1 in cards1:
        max_score[index] = max(max_score[index], number1 * number2)
max_score.sort(reverse=True)
print(max_score[K])