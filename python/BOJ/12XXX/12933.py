"""
https://www.acmicpc.net/problem/12933
12933.오리
실버4
풀이1.72ms
"""


def solve():
    count = [0] * 5
    answer = 0
    for char in input():
        if char == 'q':
            count[0] += 1
            answer = max(answer, count[0])
        elif char == 'u':
            count[1] += 1
            if count[0] < count[1]:
                return -1
        elif char == 'a':
            count[2] += 1
            if count[1] < count[2]:
                return -1
        elif char == 'c':
            count[3] += 1
            if count[2] < count[3]:
                return -1
        elif char == 'k':
            if not count[3]:
                return -1
            for i in range(4):
                count[i] -= 1

    if count[0]:
        return -1

    return answer


print(solve())