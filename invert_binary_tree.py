"""Given the root of a binary tree, invert the tree, and return its root."""


def invertTree(self, root):
    if not root:
        return None
    x = root.left
    root.left = root.right
    root.right = x
    self.invertTree(root.left)
    self.invertTree(root.right)
    return root