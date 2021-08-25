"""
https://www.acmicpc.net/problem/1525
1525.퍼즐
골드2
풀이1.1244ms
"""
from collections import deque
from collections import defaultdict


def solve(puzzle):
    q = deque([(puzzle, 0)])
    visited = defaultdict(bool)
    visited[puzzle] = True

    while q:
        puzzle, count = q.popleft()

        if puzzle == '123456780':
            print(count)
            return

        index = puzzle.find('0')

        if index >= 3:
            swap_puzzle = list(puzzle)
            swap_puzzle[index], swap_puzzle[index - 3] = swap_puzzle[index - 3], swap_puzzle[index]
            next_puzzle = ''.join(map(str, swap_puzzle))

            if not visited[next_puzzle]:
                visited[next_puzzle] = True
                q.append((next_puzzle, count + 1))

        if index <= 5:
            swap_puzzle = list(puzzle)
            swap_puzzle[index], swap_puzzle[index + 3] = swap_puzzle[index + 3], swap_puzzle[index]
            next_puzzle = ''.join(map(str, swap_puzzle))

            if not visited[next_puzzle]:
                visited[next_puzzle] = True
                q.append((next_puzzle, count + 1))

        if (index + 1) % 3 != 0:
            swap_puzzle = list(puzzle)
            swap_puzzle[index], swap_puzzle[index + 1] = swap_puzzle[index + 1], swap_puzzle[index]
            next_puzzle = ''.join(map(str, swap_puzzle))

            if not visited[next_puzzle]:
                visited[next_puzzle] = True
                q.append((next_puzzle, count + 1))

        if index % 3 != 0:
            swap_puzzle = list(puzzle)
            swap_puzzle[index], swap_puzzle[index - 1] = swap_puzzle[index - 1], swap_puzzle[index]
            next_puzzle = ''.join(map(str, swap_puzzle))

            if not visited[next_puzzle]:
                visited[next_puzzle] = True
                q.append((next_puzzle, count + 1))
    print(-1)


puzzle = ''
for _ in range(3):
    for num in input().split():
        puzzle += str(num)
solve(puzzle)
