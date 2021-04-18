"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        result = list()
        def level_helper(node, level):
            if not node:
                return None
            if len(result)<=level:
                result.append([])
            result[level].append(node.val)
            for leaf in node.children:
                level_helper(leaf,level+1)
        if root:
            level_helper(root,0)
        return result