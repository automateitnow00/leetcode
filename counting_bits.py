"""
Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), 
ans[i] is the number of 1's in the binary representation of i.
"""

#my answer
def countBits(n):
    ans = []
    for i in range(n + 1):
        x = list(bin(i)[2:]).count("1")
        ans.append(x)

    return ans

n = 50000
print(countBits(n))