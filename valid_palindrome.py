"""
A phrase is a palindrome if, 
after converting all uppercase letters into lowercase letters and 
removing all non-alphanumeric characters, 
it reads the same forward and backward. 
Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.
"""
#my solution
def isPalindrome(s: str) -> bool:
    """
    chars = []
    for i in s:
        if i.isalnum():
            chars.append(i.lower())
    """

    chars = "".join(c.lower() for c in s if c.isalnum())
    #print(chars)
    
    i = 0 
    j = len(chars) - 1
    while i < j:
        if chars[i] != chars[j]:
            return False
        i += 1
        j -= 1
    return True

x = "A man, a plan, a canal: Panama"
out = isPalindrome(x)
print(out)