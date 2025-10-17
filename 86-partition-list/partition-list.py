# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        before = ListNode(0)
        after = ListNode(0)

        b = before
        a = after
        curr = head

        while curr :
            nxt = curr.next
            curr.next = None

            if curr.val < x :
                b.next = curr
                b = curr

            else :
                a.next = curr
                a = curr
            
            curr = nxt

        b.next = after.next

        return before.next
