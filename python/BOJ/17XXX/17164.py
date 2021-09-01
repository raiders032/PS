"""
https://www.acmicpc.net/problem/17164
17164.Rainbow Beads
실버4
풀이1.248ms
"""
N = int(input())
beads = list(input())
left = 0
right = 0
answer = 1

while right < N - 1:

    if beads[right] == 'R':
        if beads[right + 1] == 'B':
            right += 1
        else:
            right += 1
            left = right
    elif beads[right] == 'B':
        if beads[right + 1] == 'R':
            right += 1
        else:
            right += 1
            left = right
    elif beads[right] == 'V':
        right += 1
        left = right

    answer = max(answer, right - left + 1)

print(answer)
