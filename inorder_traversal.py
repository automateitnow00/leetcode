"""Given the root of a binary tree, return the inorder traversal of its nodes' values.

"""


def inorderTraversal(self, root):
    res = []
    def trav(start, res):
        if start:
            trav(start.left, res)
            res.append(start.val)
            trav(start.right, res)
        return res
    return trav(root, res)