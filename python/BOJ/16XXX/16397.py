"""
https://www.acmicpc.net/problem/16397
16397.탈출
풀이1.228ms
"""
from collections import deque
from collections import defaultdict


def solve(num):
    q = deque([(num, 0)])
    visited = defaultdict(bool)
    visited[num] = True
    while q:
        num, count = q.popleft()
        if count > T:
            break

        if num == G:
            print(count)
            return

        if num + 1 <= 99999 and not visited[num + 1]:
            visited[num + 1] = True
            q.append((num + 1, count + 1))

        if 0 < num and 2 * num <= 99999:
            next_num = int(str(int(str(2 * num)[0]) - 1) + str(2 * num)[1:])
            if visited[next_num]:
                continue
            visited[next_num] = True
            q.append((next_num, count + 1))

    print("ANG")


N, T, G = map(int, input().split())
solve(N)