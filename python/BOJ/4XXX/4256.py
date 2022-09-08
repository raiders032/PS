"""
https://www.acmicpc.net/problem/4256
4256.트리
풀이1.2292ms
"""
import sys
input = sys.stdin.readline


def post_order(root, start, end):
    if start > end:
        return

    for root_index in range(start, end):
        if in_order[root_index] == pre_order[root]:
            post_order(root + 1, start, root_index)
            post_order(root + root_index + 1 - start, root_index + 1, end)
            print(pre_order[root], end=' ')


for _ in range(int(input())):
    N = int(input())
    pre_order = list(map(int, input().split()))
    in_order = list(map(int, input().split()))
    post_order(0, 0, N)
    print()