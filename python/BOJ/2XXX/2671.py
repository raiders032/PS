"""
https://www.acmicpc.net/problem/2671
2671.잠수함식별
풀이1.68ms
"""


def solve(index):
    if index == 0:
        return 1

    result = 0
    if string[index - 2:index] == "01":
        result += solve(index - 2)

    is_valid = True
    one_count = 0
    index -= 1
    while index >= 0 and string[index] == '1':
        index -=1
        one_count += 1

    if not one_count:
        is_valid = False

    zero_count = 0
    while is_valid and index >= 0 and string[index] == '0':
        index -= 1
        zero_count += 1

    if zero_count < 2:
        is_valid = False

    if index == -1 or index >= 0 and string[index] != '1':
        is_valid = False

    if is_valid:
        result += solve(index)

    return result


string = input()
print("SUBMARINE" if solve(len(string)) else "NOISE")