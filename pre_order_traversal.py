"""Given the root of a binary tree, return the preorder traversal of its nodes' values."""



def preorderTraversal(self, root):
    res = []
    def trav(start, res):
        if start:
            res.append(start.val)
            trav(start.left, res)
            trav(start.right, res)
        return res
    return trav(root, res)