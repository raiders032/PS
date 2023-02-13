"""
https://www.acmicpc.net/problem/15831
15831.준표의 조약돌
풀이1.356ms
"""
import sys

input = sys.stdin.readline

n, b, w = map(int, input().split())
stones = list(input().rstrip())
left, right = 0, 0
w_count = 1 if stones[0] == 'W' else 0
b_count = 1 if stones[0] == 'B' else 0
answer = 0

while right < n:
    if w_count >= w and b_count <= b:
        answer = max(answer, right - left + 1)

    if b_count > b:
        if stones[left] == 'W':
            w_count -= 1
        else:
            b_count -= 1
        left += 1

    else:
        right += 1

        if right < n and stones[right] == 'W':
            w_count += 1
        else:
            b_count += 1

print(answer)
