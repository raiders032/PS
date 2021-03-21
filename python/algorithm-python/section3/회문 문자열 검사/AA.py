def isPalindrome(string):
    string = str(string).lower()
    length = len(string)
    for i in range(length//2):
        if string[i] != string[length - i - 1]:
            return False
    return True


n = int(input())
for i in range(n):
    string = input()
    if isPalindrome(string):
        print("#%d YES" % (i+1))
    else:
        print("#%d NO" % (i+1))
