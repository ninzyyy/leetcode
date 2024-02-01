
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: [TreeNode], q: [TreeNode]) -> bool:

        # Both nodes do not exist
        if (not p) and (not q):
            return True

        # One node exists and the other node does not
        if (not p) or (not q):
            return False

        # Value of nodes is different
        if p.val != q.val:
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

    def isSameTreeIter(self, p: [TreeNode], q: [TreeNode]) -> bool:

        stack = [[p, q]]

        while stack:

            first, second = stack.pop()

            if not first and not second:
                continue

            if not first or not second:
                return False

            if first.val != second.val:
                return False

            stack.append([first.left, second.left])
            stack.append([first.right, second.right])

        return True