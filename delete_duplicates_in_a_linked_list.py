"""Given the head of a sorted linked list, 
delete all duplicates such that each element appears only once.
 Return the linked list sorted as well."""


#my solution
def deleteDuplicates(self, head):
    nums = dict()
    prev = head
    start = head
    while start != None:
        if start.val not in nums:
            nums[start.val] = 1
            prev = start
            start = start.next
        elif start.val in nums:
            temp = start
            start = start.next
            prev.next = start
            temp.next = None
        

    return head