"""
https://www.acmicpc.net/problem/22945
22945.팀 빌딩
풀이1.140ms
"""
import sys
input = sys.stdin.readline

n = int(input())
developers = list(map(int, input().split()))
left = 0
right = n - 1
answer = 0

while left != right:
    answer = max(answer, (right - left - 1) * min(developers[left], developers[right]))

    if developers[left] <= developers[right]:
        left += 1
    else:
        right -= 1

print(answer)