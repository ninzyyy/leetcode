
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, list1: [ListNode], list2: [ListNode]) -> [ListNode]:

        # Initialize dummy node and carry over number
        dummy = ListNode()
        tail = dummy
        carry = 0

        while list1 or list2 or carry:

            # Get values of the nodes (0 if node does not exist)
            v1 = list1.val if list1 else 0
            v2 = list2.val if list2 else 0

            # Get added value and carry over value
            val = v1 + v2 + carry
            carry = val // 10
            val = val % 10

            # Set next dummy node's added value
            tail.next = ListNode(val)
            tail = tail.next

            # Move list1 and list2 to next respective nodes
            list1 = list1.next if list1 else None
            list2 = list2.next if list2 else None

        return dummy.next
