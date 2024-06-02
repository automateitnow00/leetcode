"""
Given an array of integers nums and an integer target,
return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, 
and you may not use the same element twice.

You can return the answer in any order.
"""
#neetcode solution
def twoSum(nums, target: int):
    val = dict()
    for i in range(len(nums)):
        val[nums[i]] = i

    for i in range(len(nums)):
        x = target - nums[i]
        if x in val and val[x] != i:
            return sorted([val[x], i])
    return None
            
a = [1,2,3]
tar = 4
y = twoSum(a, tar)
print(y)

