"""
https://school.programmers.co.kr/learn/courses/30/lessons/17686
[3차] 파일명 정렬
풀이1.100점
"""


def get_head_number(name):
    head, number = '', ''
    i = 0

    while i < len(name) and not name[i].isdigit():
        head += name[i]
        i += 1

    while i < len(name) and name[i].isdigit():
        number += name[i]
        i += 1

    return head.lower(), int(number)


def solution(files):
    answer = []
    filenames = list()
    for i in range(len(files)):
        head, number = get_head_number(files[i])
        filenames.append((head, number, i, files[i]))

    for filename in sorted(filenames):
        print(filename)
        answer.append(filename[3])

    return answer


print(solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]))
