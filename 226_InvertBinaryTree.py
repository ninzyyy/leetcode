class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: [TreeNode]) -> [TreeNode]:

        if not root:
            return None

        temp_left, temp_right = root.left, root.right
        root.right = temp_left
        root.left = temp_right

        self.invertTree(root.right)
        self.invertTree(root.left)

        return root
