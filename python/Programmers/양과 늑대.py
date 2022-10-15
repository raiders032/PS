"""
https://school.programmers.co.kr/learn/courses/30/lessons/92343
양과 늑대
풀이1.100점
"""


def solution(info, edges):
    def visit(node, sheep_count, wolf_count, next_visit):
        nonlocal answer
        sheep_count += info[node] ^ 1
        wolf_count += info[node]

        if sheep_count <= wolf_count:
            return
        else:
            answer = max(answer, sheep_count)

        for child in list(next_visit):
            temp = set(next_visit)
            temp.remove(child)
            for c in tree[child]:
                temp.add(c)
            visit(child, sheep_count, wolf_count, temp)

    answer = 0
    n = len(info)
    tree = [list() for _ in range(n)]

    for edge in edges:
        parent, child = edge
        tree[parent].append(child)

    visit(0, 0, 0, set(tree[0]))

    return answer


print(solution([0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1],
               [[0, 1], [1, 2], [1, 4], [0, 8], [8, 7], [9, 10], [9, 11], [4, 3], [6, 5], [4, 6], [8, 9]]))

print(solution([0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0],
               [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [4, 8], [6, 9], [9, 10]]))
