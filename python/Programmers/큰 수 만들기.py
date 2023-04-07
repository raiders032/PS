"""
https://programmers.co.kr/learn/courses/30/lessons/42883
큰 수 만들기
레벨2
풀이3
"""


def solution(numbers, k):
    selected = [numbers[0]]

    for index in range(1, len(numbers)):
        while k and selected and selected[-1] < numbers[index]:
            selected.pop()
            k -= 1
        selected.append(numbers[index])

    if k:
        selected = selected[:-k]

    return ''.join(selected)


print(solution("123456", 1))
