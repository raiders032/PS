"""
https://www.acmicpc.net/problem/22945
22945.팀 빌딩
풀이2.156ms
"""
import sys
input = sys.stdin.readline

n = int(input())
score = list(map(int, input().split()))
low = 0
high = n - 1
answer = min(score[low], score[high]) * (high - low - 1)

while low < high:
    team_score = min(score[low], score[high]) * (high - low - 1)
    answer = max(answer, team_score)

    if score[low] <= score[high]:
        low += 1
    else:
        high -= 1

print(answer)
