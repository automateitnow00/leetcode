s = "egg"
t = "foo"


def isIsomorphic(s: str, t: str) -> bool:
        a = dict()
        b = dict()
        if len(s) == len(t):
            i = 0
            while i < len(s):
                if s[i] not in a:
                    a[s[i]] = t[i]
                elif s[i] in a and a[s[i]] != t[i]:
                    return False
                i += 1
            j = 0 
            while j < len(t):
                if t[j] not in b:
                    b[t[j]] = s[j]
                elif t[j] in b and b[t[j]] != s[j]:
                    return False
                j += 1
            return True
        else:
            return False
        
X = isIsomorphic(s,t)
print(X)