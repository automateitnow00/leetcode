"""Given the head of a singly linked list, return true if it is a palindrome or false otherwise."""
#my solution
def isPalindrome(head) -> bool:
    start = head
    nums = []
    while start != None:
        nums.append(start.val)
        start = start.next

    i = 0
    j = len(nums) - 1
    while i < j:
        if nums[i] != nums[j]:
            return False
        i += 1
        j -= 1
    return True