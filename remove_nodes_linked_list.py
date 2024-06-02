"""Given the head of a linked list and an integer val, 
remove all the nodes of the linked list that has Node.val == val,
 and return the new head."""


class ListNode:
    pass


def removeElements(self, head, val: int):
    nodes = []
    start = head
    while start != None:
        if start.val != val:
            nodes.append(start.val)
        start = start.next

    head = None
    while len(nodes) > 0:
        if head == None:
            head = ListNode(nodes.pop(0))
            start = head
        else:
            start.next = ListNode(nodes.pop(0))
            start = start.next

    return head