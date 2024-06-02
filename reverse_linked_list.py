"""Given the head of a singly linked list, reverse the list, and return the reversed list."""


def reverseList(self, head):
    nodes = []
    start = head
    while start != None:
        nodes.append(start)
        start = start.next
        nodes[-1].next = None
    print(nodes)

    head = None
    if len(nodes) > 0: 
        head = nodes.pop()
        start = head
        while len(nodes) > 0:
            start.next = nodes.pop()
            #prev = start
            start = start.next
    
    #prev.next = None
    return head