"""
https://school.programmers.co.kr/learn/courses/30/lessons/42892
길 찾기 게임
풀이1.100점
"""
import sys
sys.setrecursionlimit(10 ** 6)


def solution(nodeinfo):
    def insert_node(parent_node_number, node):
        if node[0] < node_position[parent_node_number][0]:
            if not tree[parent_node_number][0]:
                tree[parent_node_number][0] = node[2]
                return
            insert_node(tree[parent_node_number][0], node)
        else:
            if not tree[parent_node_number][1]:
                tree[parent_node_number][1] = node[2]
                return
            insert_node(tree[parent_node_number][1], node)

    def pre_order(node_number):
        answer[0].append(node_number)
        if tree[node_number][0]:
            pre_order(tree[node_number][0])
        if tree[node_number][1]:
            pre_order(tree[node_number][1])

    def post_order(node_number):
        if tree[node_number][0]:
            post_order(tree[node_number][0])
        if tree[node_number][1]:
            post_order(tree[node_number][1])
        answer[1].append(node_number)

    n = len(nodeinfo)
    answer = [[], []]
    nodes = []
    node_position = dict()
    tree = [[0, 0] for _ in range(n + 1)]
    for i, (x, y) in enumerate(nodeinfo):
        nodes.append((x, y, i + 1))
        node_position[i + 1] = (x, y)

    nodes.sort(key=lambda x: -x[1])
    root_node_number = nodes[0][2]
    for node in nodes[1:]:
        insert_node(root_node_number, node)

    pre_order(root_node_number)
    post_order(root_node_number)
    return answer


print(solution([[5, 3], [11, 5], [13, 3], [3, 5], [6, 1], [1, 3], [8, 6], [7, 2], [2, 2]]))
