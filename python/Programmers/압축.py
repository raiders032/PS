"""
https://school.programmers.co.kr/learn/courses/30/lessons/17684
[3차] 압축
풀이1.100점
"""


def solution(msg):
    answer = []
    dictionary = dict()
    for i in range(1, 27):
        dictionary[chr(i - 1 + ord('A'))] = i
    last_sequence = 27

    i = 0
    while i < len(msg):
        w = msg[i]
        while i + 1 < len(msg) and w + msg[i + 1] in dictionary:
            w += msg[i + 1]
            i += 1

        answer.append(dictionary[w])

        if i + 1 < len(msg):
            dictionary[w + msg[i + 1]] = last_sequence
            last_sequence += 1

        i += 1

    return answer


print(solution('KAKAO'))