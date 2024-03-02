def reverse(s):
    return str(s)[::-1]


def isPalindrome(s):
    s = str(s)
    return s == reverse(s)


print(isPalindrome("iti"))
print(isPalindrome("yousef"))
print(isPalindrome(5928))
print(isPalindrome(555))
