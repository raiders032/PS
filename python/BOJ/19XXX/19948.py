"""
https://www.acmicpc.net/problem/19948
19948.음유시인 영재
풀이1.72ms
"""
import sys
input = sys.stdin.readline


def on_going():
    global i
    while i < len(poem) and poem[i] == poem[i - 1]:
        i += 1


poem = input().rstrip()
space_count = int(input())
alpha_count = list(map(int, input().split()))
title = ''
i = 0
is_title = True

while i < len(poem):
    if poem[i] == ' ':
        is_title = True
        if not space_count:
            title = -1
            break
        space_count -= 1
    else:
        if is_title:
            if alpha_count[ord((poem[i].upper())) - ord('A')] < 2:
                title = -1
                break
            title += poem[i].upper()
            is_title = False
            alpha_count[ord((poem[i].upper())) - ord('A')] -= 2
        else:
            if not alpha_count[ord((poem[i].upper())) - ord('A')]:
                title = -1
                break
            alpha_count[ord((poem[i].upper())) - ord('A')] -= 1
    i += 1
    on_going()

print(title)