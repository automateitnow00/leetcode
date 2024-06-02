"""
Given a non-empty array of integers nums, every element appears twice except for one. 
Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space
"""


#my solution

def singleNumber(nums):
    nums1 = nums.copy()
    nums1 = list(set(nums1))
    for i in nums1:
        if nums.count(i) == 1:
            return i
        
nums = [4,1,2,1,2]
print(singleNumber(nums))