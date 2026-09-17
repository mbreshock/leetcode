# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(root):
        result = []
        stack = []
        curr = root
        
        while curr or stack:
            # Go as far left as possible, stacking nodes along the way
            while curr:
                stack.append(curr)
                curr = curr.left
            
            # Backtrack: pop the node, record it, then go right
            curr = stack.pop()
            result.append(curr.val)
            curr = curr.right
        
        return result