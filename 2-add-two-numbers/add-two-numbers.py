# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        res = dummy

        sm = flag = 0

        while l1 or l2 or flag :
            sm = flag

            if l1 :
                sm += l1.val
                l1 = l1.next
            if l2 :
                sm += l2.val
                l2 = l2.next

            num = sm % 10
            flag = sm // 10

            dummy.next = ListNode(num)
            dummy = dummy.next

        return res.next