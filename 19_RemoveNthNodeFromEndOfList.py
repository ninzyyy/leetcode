
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: [ListNode], n: int) -> [ListNode]:

        dummy = ListNode(0, head)
        left = dummy
        right = head

        # Move the right pointer nth away from left
        while n:
            right = right.next
            n -= 1

        # Move pointers until left is at nth from tail (and right is None)
        while right:
            left = left.next
            right = right.next

        # Skip the nth node
        left.next = left.next.next
        return dummy.next
