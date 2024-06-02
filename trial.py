def findMin(nums):
    res = nums[0]
    l , r = 0, len(nums) - 1
    while l <= r:
        if nums[l] < nums[r]:
            res = min(res, nums[l])
            return res
        m = l + ((r - l) // 2)
        if (nums[m] < nums[l]): 
            r = m - 1
        elif nums[m] >= nums[l]: l = m + 1
    return res

nums = [3, 4,5 ,1,2]
print(findMin(nums))