"""
https://www.acmicpc.net/problem/15664
15664.N과 M (10)
실버2
풀이1.68ms
"""


def dfs(idx):
    if len(selected) == M:
        if tuple(selected) in visited:
            return

        for num in selected:
            print(num, end=' ')
        print()
        visited.add(tuple(selected))
        return

    for i in range(idx, N):
        selected.append(nums[i])
        dfs(i + 1)
        selected.pop()


N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
selected = []
visited = set()
dfs(0)



