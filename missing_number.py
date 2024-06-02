nums = [3, 0, 1]

#my solution is using sets but it need O(n) space 
def missingNumber(nums) -> int:
    numb = set([i for i in range(0, len(nums) + 1)])
    nums = set(nums)
    X = numb.difference(nums)
    for i in X:
        return i

X = missingNumber(nums)
print(X)  
#there is the sum solution where take the sum of the array 
#and you take the sum of 0 to n integers the difference between these is going to be the missing number
def missing(nums):
    res1 = 0
    for i in nums:
        res1 += i
    
    n = len(nums)
    res2 = (n * (n + 1))/2  #gauss formula
    return int(res2 - res1)

X = missing(nums)
print(X) 

    
#you can use XOR also