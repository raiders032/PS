"""
https://www.acmicpc.net/problem/7682
7682.틱택토
풀이1.64ms
"""
from collections import Counter
import sys


def win(xo):
    for row in ttt:
        if row == [xo, xo, xo]:
            return True

    for col in zip(*ttt):
        if col == (xo, xo, xo):
            return True

    if ttt[0][0] == ttt[1][1] == ttt[2][2] == xo:
        return True

    if ttt[0][2] == ttt[1][1] == ttt[2][0] == xo:
        return True

    return False


input = sys.stdin.readline
answer = []

while True:
    ttt = input().rstrip()

    if ttt == 'end':
        break

    ttt = list(ttt)
    character_count = Counter(ttt)
    ttt = [ttt[:3], ttt[3: 6], ttt[6:]]

    if character_count['X'] + character_count['O'] < 5:
        answer.append("invalid")
        continue

    if character_count['X'] - character_count['O'] < 0 or character_count['X'] - character_count['O'] > 1:
        answer.append("invalid")
        continue

    if character_count['X'] + character_count['O'] == 9:
        if not win('O'):
            answer.append('valid')
            continue

    elif character_count['X'] == character_count['O']:
        if win('O') and not win('X'):
            answer.append('valid')
            continue

    else:
        if win('X') and not win('O'):
            answer.append('valid')
            continue

    answer.append('invalid')

print('\n'.join(answer))

"""
XXXXOOXOO
XOXOXOXO.
XOXOXOX..
XO.X.OXO.
XOXOXOXOX
end
---
valid
invalid
valid
invalid
valid

"""
