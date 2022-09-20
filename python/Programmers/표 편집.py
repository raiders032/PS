"""
https://school.programmers.co.kr/learn/courses/30/lessons/81303
표 편집
풀이1.100점
"""


def solution(n, current, cmd):
    answer = ['O'] * n
    deleted = []
    linked_list = dict()
    for i in range(n):
        linked_list[i] = [i - 1, i + 1]
    linked_list[0] = [None, 1]
    linked_list[n - 1] = [n - 2, None]

    for command in cmd:
        if command.startswith('D'):
            command, number = command.split()
            for _ in range(int(number)):
                current = linked_list[current][1]
        elif command.startswith('U'):
            command, number = command.split()
            for _ in range(int(number)):
                current = linked_list[current][0]
        elif command.startswith('C'):
            pre, next = linked_list[current]
            deleted.append([current, pre, next])
            answer[current] = 'X'

            if next is None:
                linked_list[pre][1] = None
                current = pre
            elif pre is None:
                linked_list[next][0] = None
                current = next
            else:
                linked_list[pre][1] = next
                linked_list[next][0] = pre
                current = next

        elif command.startswith('Z'):
            node, pre, next = deleted.pop()
            answer[node] = 'O'
            if pre is not None:
                linked_list[pre][1] = node
            if next is not None:
                linked_list[next][0] = node

    return ''.join(answer)


print(solution(8, 2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z"]))
# print(solution(8, 2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z", "U 1", "C"]))
