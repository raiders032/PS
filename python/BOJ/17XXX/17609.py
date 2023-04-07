"""
https://www.acmicpc.net/problem/17609
17609.회문
풀이1.
"""
import sys

input = sys.stdin.readline

for _ in range(int(input())):
    string = input().rstrip()
    if string == string[::-1]:
        print(0)
        continue

    is_valid = True
    count = 0
    head, tail = 0, len(string) - 1

    while head < tail:
        if count >= 2:
            is_valid = False
            break

        if string[head] == string[tail]:
            head += 1
            tail -= 1
            continue

        if head + 1 == tail:
            count += 1
            continue

        if string[head] == string[tail - 1]:
            head += 1
            tail -= 2
            count += 1
        elif string[head + 1] == string[tail]:
            head += 2
            tail -= 1
            count += 1
        else:
            is_valid = False
            break

    if is_valid:
        print(1)
    else:
        print(2)

"""
21
abbab
aab
aaab
aaaab
aaaaab
aaaaaab
axaaxaa
abcddadca
aabcbcaa
ababbabaa
abca
babba
sumumuus
XYXYAAYXY
abc
cccfccfcc
abcddcdba
ppbpppb
aabcdeddcba
aabab
aapqbcbqpqaa

1
1
1
1
1
1
1
2
1
1
1
1
1
1
2
1
1
2
2
2
1
"""