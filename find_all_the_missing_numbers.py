def findDisappearedNumbers(nums):
    real = set([i for i in range(1, len(nums) + 1)])
    print(real)
    nums = set(nums)
    return list(real - nums)

nums = [4,3,2,7,8,2,3,1]
print(findDisappearedNumbers(nums))