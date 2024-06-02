"""Given the roots of two binary trees p and q, 
write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, 
and the nodes have the same value."""

#my solution
def isSameTree(p, q) -> bool:
    def trav(start, res = []):
        if start:
            trav(start.left, res)
            trav(start.right, res)
            res.append(start.val)
        else:
            res.append(None)
        return res

    tree1 = trav(p)
    tree2 = trav(q, res = [])
    #print(tree1)
    #print(tree2)
    return (tree1 == tree2)