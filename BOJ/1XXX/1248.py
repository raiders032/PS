"""
1248. 맞춰봐 골드3
백트래킹
"""

import sys

sys.setrecursionlimit(10000)

N = int(sys.stdin.readline())
signs = list(sys.stdin.readline().rstrip())
selected_nums = []
left = 0
right = N
tmp_N = N
signs_arr = []
for i in range(N):
    signs_arr.append([0] * i + signs[left:right])
    left = right
    tmp_N -= 1
    right = right + tmp_N


def dfs(level):
    if level == N:
        for x in selected_nums:
            print(x, end=' ')
        sys.exit(0)
    for num in range(-10, 11):
        selected_nums.append(num)
        for idx in range(level + 1):
            selected_sum = sum(selected_nums[idx:level + 1])
            if signs_arr[idx][level] == '0' and selected_sum != 0:
                selected_nums.pop()
                break
            elif signs_arr[idx][level] == '+' and selected_sum <= 0:
                selected_nums.pop()
                break
            elif signs_arr[idx][level] == '-' and selected_sum >= 0:
                selected_nums.pop()
                break
        else:
            dfs(level + 1)
            selected_nums.pop()


dfs(0)
