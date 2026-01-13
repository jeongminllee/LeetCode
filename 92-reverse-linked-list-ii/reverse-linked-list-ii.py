# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(-501, head)
        curr1 = dummy
        length = right - left + 1

        for _ in range(left) :
            curr1 = curr1.next

        curr2 = curr1

        stack = []

        for _ in range(length) :
            stack.append(curr1.val)
            curr1 = curr1.next

        while stack :
            v = stack.pop()
            curr2.val = v
            curr2 = curr2.next

        return dummy.next