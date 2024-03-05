import collections, Optional, List

class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        solution = []
        queue = collections.deque()
        queue.append(root)

        while queue:
            len_q = len(queue)
            layer = []

            for i in range(len_q):
                node = queue.popleft()

                if node:
                    layer.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)

            solution.append(layer)

        return [layer[-1] for layer in solution if layer]