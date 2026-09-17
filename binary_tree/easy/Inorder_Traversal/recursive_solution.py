# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode | None) -> list[int]:
        result = []

        def node_check(node): 
            if node is None: 
                return
            
            node_check(node.left)
            result.append(node.val)
            node_check(node.right)
        
        node_check(root)
        return result