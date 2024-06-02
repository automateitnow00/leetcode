"""Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.

"""

class ListNode:
    pass


def middleNode(self, head):
    length = 0
    nodes = []
    start = head
    while start != None:
        length += 1
        nodes.append(start)
        start = start.next

    return nodes[length//2]