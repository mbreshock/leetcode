# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: TreeNode | None) -> int:
        max_depth = 1
        def depth_node(node: TreeNode | None, d): 
            nonlocal max_depth
            if node is None: 
                return
            if d > max_depth: 
                max_depth = d
            depth_node(node.left, d+1) 
            depth_node(node.right, d+1)

        depth_node(root, 1)
        return max_depth


# This failed on the following test case: 
# root = []
# Code Output: 1
# Expected: 0