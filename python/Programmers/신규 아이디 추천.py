"""
https://school.programmers.co.kr/learn/courses/30/lessons/72410
신규 아이디 추천
풀이1.100점
"""
import re


def solution(new_id):
    answer = new_id.lower()
    answer = re.sub('[^a-z0-9-_.]*', '', answer)
    answer = re.sub('\.+', '.', answer)
    answer = re.sub('^\.|\.$', '', answer)
    answer = 'a' if not answer else answer
    answer = answer[:15]
    answer = re.sub('\.$', '', answer)
    while len(answer) <= 2:
        answer += answer[-1]

    return answer