# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
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

            flag = sm // 10
            num = sm % 10

            res.next = ListNode(num)
            res = res.next

        return dummy.next