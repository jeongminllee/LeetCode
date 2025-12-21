# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        myhead = ListNode(val=-101, next=head)
        prev = myhead
        node = head

        while node and node.next :
            if node.val == node.next.val :
                while node.next and node.val == node.next.val :
                    node = node.next
                prev.next = node.next
        
            else :
                prev = prev.next

            node = node.next

        return myhead.next