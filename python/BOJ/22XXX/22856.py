"""
https://www.acmicpc.net/problem/22856
22856.트리 순회
풀이1.200ms
"""
import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)


def get_depth(node):
    if tree[node][1] != -1:
        return 1 + get_depth(tree[node][1])
    return 1


n = int(input())
tree = [0] * (n + 1)

for _ in range(n):
    parent, left_child, right_child = map(int, input().split())
    tree[parent] = (left_child, right_child)

print(2 * n - get_depth(1) - 1)
