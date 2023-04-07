"""
https://www.acmicpc.net/problem/2922
2922.즐거운 단어
풀이1.572ms
"""


def get_count(index, count):
    if index == len(word):
        serial_count = 1
        for i in range(1, len(word)):
            if serial_count == 3:
                break
            if 'V' == word[i] == word[i - 1]:
                serial_count += 1
            elif 'V' == word[i] != word[i - 1]:
                serial_count = 1
            else:
                if word[i - 1] == 'L' or word[i - 1] == 'C':
                    serial_count += 1
                else:
                    serial_count = 1

        if serial_count == 3 or 'L' not in word:
            return 0
        return count

    if word[index] != '_':
        return get_count(index + 1, count)

    result = 0

    word[index] = 'L'
    result += get_count(index + 1, count)
    word[index] = '_'

    word[index] = 'C'
    result += get_count(index + 1, count * 20)
    word[index] = '_'

    word[index] = 'V'
    result += get_count(index + 1, count * 5)
    word[index] = '_'

    return result


word = []
vowels = ('A', 'E', 'I', 'O', 'U')
for char in input():
    if char in vowels:
        word.append('V')
    elif char == 'L':
        word.append('L')
    elif char == '_':
        word.append('_')
    else:
        word.append('C')
print(get_count(0, 1))
