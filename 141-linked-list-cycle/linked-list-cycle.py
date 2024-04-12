# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        node = head

        while node and node.next :
            head = head.next
            node = node.next.next
            if head is node :
                return True

        return False