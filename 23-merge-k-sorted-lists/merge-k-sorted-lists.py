# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0 :
            return None

        dummy = ListNode(-10001)
        curr = dummy

        for head in lists :
            curr.next = head
            while curr and curr.next :
                curr = curr.next
        
        if dummy.next is None or dummy.next.next is None :
            return dummy.next
        
        return self.divide(dummy.next)

    def divide(self, head) :
        if head is None or head.next is None :
            return head

        slow, fast = head, head.next

        while fast and fast.next :
            slow = slow.next
            fast = fast.next.next

        mid = slow.next
        slow.next = None

        left = self.divide(head)
        right = self.divide(mid)

        return self.merge(left, right)

    def merge(self, left, right) :
        res = ListNode(-10001)
        curr = res

        while left and right :
            if left.val < right.val :
                curr.next = left
                left = left.next
            else :
                curr.next = right
                right = right.next

            curr = curr.next

        curr.next = left or right

        return res.next