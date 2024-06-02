"""Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].

Return the array in the form [x1,y1,x2,y2,...,xn,yn].

"""

nums = [2,5,1,3,4,7]
n = 3

#my solution
def shuffle(nums, n):
    i = 0
    j = n
    res = []
    while i < n and j < len(nums):
        res.append(nums[i])
        res.append(nums[j])
        i += 1
        j += 1
    return res

X = shuffle(nums, n)
print(X)
