"""
https://www.acmicpc.net/problem/1967
1967.트리의 지름
풀이2.104ms
"""
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

def make_max_height(node):
    if max_height[node] != -1:
        return max_height[node]

    max_height[node] = 0
    for child, weight in tree[node]:
        max_height[node] = max(max_height[node], make_max_height(child) + weight)

    return max_height[node]


def get_tree_radius(node):
    if tree_radius[node] != -1:
        return tree_radius[node]

    tree_radius[node] = 0
    height = []
    for child, weight in tree[node]:
        tree_radius[node] = max(tree_radius[node], get_tree_radius(child))
        height.append(max_height[child] + weight)

    height.sort(reverse=True)
    tree_radius[node] = max(tree_radius[node], sum(height[:2]))

    return tree_radius[node]


N = int(input())
tree = [list() for _ in range(N + 1)]
max_height = [-1] * (N + 1)
tree_radius = [-1] * (N + 1)
for _ in range(N - 1):
    parent, child, weight, = map(int, input().split())
    tree[parent].append((child, weight))

make_max_height(1)
print(get_tree_radius(1))