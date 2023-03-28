"""
https://www.acmicpc.net/problem/16719
16719.ZOAC
풀이1.68ms
"""
import sys

input = sys.stdin.readline

chars = list(input().rstrip())
answer = ["".join(chars)]

while len(chars) > 1:
    i = 0
    while i < len(chars):
        if i == len(chars) - 1:
            temp = chars[:i]
            break

        if chars[i] > chars[i + 1]:
            temp = chars[:i] + chars[i + 1:]
            break

        i += 1

    chars = temp
    answer.append("".join(chars))

print("\n".join(answer[::-1]))
