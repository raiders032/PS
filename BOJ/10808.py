# 10808번 알파벳 개수 브론즈2
string = input()
count = [0] * 26
for x in string:
    count[ord(x) - ord('a')] += 1

for x in count:
    print(x, end=' ')
