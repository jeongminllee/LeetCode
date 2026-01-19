# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0 :
            return None

        # Merge Multi to Single Linked List
        dummy = ListNode(-10001)
        curr = dummy

        # Merge
        for head in lists :
            curr.next = head
            # Move Pointer 
            while curr and curr.next :
                curr = curr.next
        
        # Pruning
        if dummy.next is None or dummy.next.next is None :
            return dummy.next
        
        # Divde
        return self.divide(dummy.next)

    def divide(self, head) :
        # Return condition
        if head is None or head.next is None :
            return head
        
        # Find mid
        slow, fast = head, head.next

        while fast and fast.next :
            slow = slow.next
            fast = fast.next.next

        mid = slow.next
        slow.next = None

        # Divided Single node
        left = self.divide(head)
        right = self.divide(mid)

        # Merge
        return self.merge(left, right)

    def merge(self, left, right) :
        res = ListNode(-10001)
        curr = res

        # Merge
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