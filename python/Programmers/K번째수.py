"""
https://programmers.co.kr/learn/courses/30/lessons/42748
K번째수
레벨1
정렬
풀이1
"""


def solution(array, commands):
    answer = []
    for command in commands:
        left, right, k = command[0], command[1], command[2]
        sorted_list = sorted(list(array[left - 1: right]))
        answer.append(sorted_list[k - 1])
    return answer


print(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))
