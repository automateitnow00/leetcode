"""Given the root of a binary tree, return the postorder traversal of its nodes' values."""




def postorderTraversal(self, root):
    res = []
    def trav(start, res):
        if start:
            trav(start.left, res)
            trav(start.right, res)
            res.append(start.val)
        return res
    return trav(root, res)