"""Given an integer array nums, rotate the array to the right by k steps, 
where k is non-negative."""


def rotate(nums, k) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    while k > 0:
        x = nums.pop()
        nums.insert(0, x)
        k -= 1

nums = [1,2,3,4,5,6,7]
k = 3
rotate(nums, k)
print(nums)