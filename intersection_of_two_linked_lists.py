"""Given the heads of two singly linked-lists headA and headB, 
return the node at which the two lists intersect.
 If the two linked lists have no intersection at all, return null."""


def getIntersectionNode(self, headA, headB):
    l1 = []
    start = headA
    while start != None:
        l1.append(start)
        start = start.next

    l2 = []
    start = headB
    while start != None:
        l2.append(start)
        start = start.next

    for i in l1:
        if i in l2:
            return i