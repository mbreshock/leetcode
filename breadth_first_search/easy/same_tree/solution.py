# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p: TreeNode | None, q: TreeNode | None) -> bool:
        queue = [(p,q)]

        while queue:
            s_p, s_q = queue.pop(0)

            if s_p is None and s_q is None: 
                continue
            if s_p is None or s_q is None: 
                return False
            if s_p.val != s_q.val: 
                return False

            queue.append((s_p.left, s_q.left))
            queue.append((s_p.right, s_q.right))

        return True