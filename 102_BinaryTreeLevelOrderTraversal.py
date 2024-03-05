import collections, List, Dict

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:

        solution = []
        queue = collections.deque()
        queue.append(root)

        while queue:
            curr_len = len(queue)
            level = []
            for i in range(curr_len):
                node = queue.popleft() # Get and remove first node from queue
                if node:
                    level.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)

            if level:
                solution.append(level)

        return solution
