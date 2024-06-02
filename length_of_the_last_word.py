"""
Given a string s consisting of words and spaces, 
return the length of the last word in the string.

A word is a maximal 
substring
 consisting of non-space characters only.
"""

#my solution
def lengthOfLastWord(s: str) -> int:
    words = s.split(' ')
    
    """
    while '' in words:
        words.remove('')
        """

    words1 = []
    for i in range(len(words)):
        if len(words[i]) != 0:
            words1.append(words[i])
    

    #print(words1)
    #print(len(words1[0]))
    return [words1, len(words1[-1])]

c = "   fly me   to   the moon  "
out = lengthOfLastWord(c)
print(out)