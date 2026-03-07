"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        graph = {}

        def dfs(node) :
            if node in graph :
                return graph[node]

            nnode = Node(node.val)
            graph[node] = nnode

            for neighbor in node.neighbors :
                nnode.neighbors.append(dfs(neighbor))

            return nnode

        return dfs(node) if node else None