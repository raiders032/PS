"""
https://www.acmicpc.net/problem/12912
12912.트리 수정
풀이1.
"""
import sys
from collections import defaultdict
input = sys.stdin.readline


def make_max_height(node, tree):
    if max_height[node] != -1:
        return max_height[node]

    max_height[node] = 0
    for child, weight in tree[node]:
        max_height[node] = max(max_height[node], make_max_height(child, tree) + weight)

    return max_height[node]


def get_tree_radius(node, tree):
    if tree_radius[node] != -1:
        return tree_radius[node]

    heights = []
    tree_radius[node] = 0
    for child, weight in tree[node]:
        tree_radius[node] = max(tree_radius[node], get_tree_radius(child, tree))
        heights.append(max_height[child] + weight)
    heights.sort(reverse=True)
    tree_radius[node] = max(tree_radius[node], sum(heights[:2]))

    return tree_radius[node]


N = int(input())
edges = [tuple(map(int, input().split())) for _ in range(N - 1)]
sheep_count = 0

for i in range(len(edges)):
    print(f'-------------{edges[i]}--------------')
    tree1 = defaultdict(list)
    tree2 = defaultdict(list)
    tree1_in_degree = defaultdict(int)
    tree2_in_degree = defaultdict(int)

    for j in range(i):
        tree1[edges[j][0]].append((edges[j][1], edges[j][2]))
        tree1_in_degree[edges[j][1]] += 1

    for j in range(i + 1, len(edges)):
        tree2[edges[j][0]].append((edges[j][1], edges[j][2]))
        tree2_in_degree[edges[j][1]] += 1

    max_height = [-1] * N
    tree_radius = [-1] * N
    root_node = 0
    if not tree1.keys():
        root_node = edges[i][0]
    for node in tree1.keys():
        if tree1_in_degree[node] == 0:
            root_node = node
            break
    make_max_height(root_node, tree1)
    tree1_radius = get_tree_radius(root_node, tree1)
    print(f'tree1_root:{root_node}, tree1:{tree1.keys()}')

    max_height = [-1] * N
    tree_radius = [-1] * N
    root_node = 0
    if not tree2.keys():
        root_node = edges[i][1]
    for node in tree2.keys():
        if tree2_in_degree[node] == 0:
            root_node = node
            break
    make_max_height(root_node, tree2)
    tree2_radius = get_tree_radius(root_node, tree2)
    print(f'tree2_root:{root_node}, tree2:{tree2.keys()}')
    print(f'tree1_radius:{tree1_radius}, tree2_radius:{tree2_radius}, edge-i:{edges[i]}')
    sheep_count = max(sheep_count, tree1_radius + tree2_radius + edges[i][2])

print(sheep_count)

