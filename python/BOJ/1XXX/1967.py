"""
https://www.acmicpc.net/problem/1967
1967.트리의 지름
풀이1.104ms
"""
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)


def get_tree_diameter(parent):
    global answer

    if not tree[parent]:
        return 0

    diameter = [0] * len(tree[parent])
    for i in range(len(tree[parent])):
        diameter[i] += get_tree_diameter(tree[parent][i][0]) + tree[parent][i][1]
    diameter.sort(reverse=True)
    answer = max(answer, sum(diameter[:2]))
    return diameter[0]


N = int(input())
tree = [list() for _ in range(N + 1)]
answer = 0
for _ in range(N - 1):
    parent, child, weight = map(int, input().split())
    tree[parent].append((child, weight))
get_tree_diameter(1)
print(answer)
