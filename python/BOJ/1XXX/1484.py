"""
https://www.acmicpc.net/problem/1484
1484.다이어트
풀이1.160ms
"""
import sys

input = sys.stdin.readline

g = int(input())
after_weight = 2
answer = []
stop = False

while not stop:
    for before_weight in range(after_weight - 1, 0, -1):
        if (after_weight + before_weight) * (after_weight - before_weight) > g:
            if before_weight == after_weight - 1:
                stop = True
            break

        if (after_weight + before_weight) * (after_weight - before_weight) == g:
            answer.append(after_weight)
            break

    after_weight += 1

print('\n'.join(map(str, answer)) if len(answer) else -1)