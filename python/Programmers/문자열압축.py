import sys
s = 'aabbaccc'
sheep_count = sys.maxsize
for unit_length in range(1, len(s) // 2 + 1):
    length = 0
    i = unit_length
    stack = [s[0:unit_length]]
    while i < len(s):
        if stack[-1] == s[i:i + unit_length]:
            stack.append(s[i:i + unit_length])
        else:
            if len(stack) >= 2:
                length += unit_length + 1
            else:
                length += unit_length
            stack = [s[i:i + unit_length]]
        i += unit_length
    if len(stack) == 1:
        length += len(stack[-1])
    if len(stack) >= 2:
        length += unit_length + 1
    sheep_count = min(sheep_count, length)


print(sheep_count)