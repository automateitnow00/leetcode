def productExceptSelf(nums):
    number_of_zeros = nums.count(0)
    if number_of_zeros > 1:
        res = [0] * len(nums)
        return res

    elif number_of_zeros == 1:
        res = [0] * len(nums)
        index = nums.index(0)
        nums.remove(0)
        mul = 1
        for i in nums:
            mul *= i
        res[index] = mul
        return res

    elif number_of_zeros == 0:
        mul = 1
        for i in nums:
            mul *= i
        res = [mul] *len(nums)
        i = 0
        while i < len(nums):
            res[i] = int(res[i]/nums[i])
            i += 1
        return res
    

nums = [1,2,3,4]
print(productExceptSelf(nums))