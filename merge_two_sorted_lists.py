"""You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. 
The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.


"""
class ListNode:
    pass

def mergeTwoLists(self, list1, list2):
    nodes = []
    start = list1
    while start != None:
        nodes.append(start.val)
        start = start.next

    start = list2
    while start != None:
        nodes.append(start.val)
        start = start.next

    nodes.sort()
    head = None

    while len(nodes) > 0:
        if head == None:
            head = ListNode(nodes.pop(0))
            start = head
        else:
            start.next = ListNode(nodes.pop(0))
            start = start.next

    return head