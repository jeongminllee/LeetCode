"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root is None :
            return root

        self.postorder(root, 0, {})
        return root

    def postorder(self, node, level:int, dct:dict) :
        node.next = None

        if node.left :
            self.postorder(node.left, level + 1, dct)
        if node.right :
            self.postorder(node.right, level + 1, dct)
        
        if level in dct.keys() :
            dct[level].next = node
        dct[level] = node
        