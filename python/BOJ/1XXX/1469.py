import sys

input = sys.stdin.readline

n = int(input())
number = list(map(int, input().split()))
sequence = [-1] * (2 * n)
answer = []


def dfs(level):
    if level == n:
        answer.append(list(sequence))
        return

    for left in range(2 * n - number[level] - 1):
        right = left + number[level] + 1

        if sequence[left] != -1 or sequence[right] != -1:
            continue

        sequence[left] = sequence[right] = number[level]
        dfs(level + 1)
        sequence[left] = sequence[right] = -1


dfs(0)
if answer:
    print(answer)
    answer.sort()
    print(' '.join(map(str, answer[0])))
else:
    print(-1)
