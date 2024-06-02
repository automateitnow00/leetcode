"""Given an integer x, return true if x is a  palindrome , and false otherwise."""


def isPalindrome(x: int) -> bool:
    x = list(str(x))
    i = 0
    j = len(x) - 1
    while i < j:
        if x[i] != x[j]:
            return False
        i += 1
        j -= 1

    return True

x = 121
print(isPalindrome(x))