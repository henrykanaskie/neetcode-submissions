# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        def dfs(root, max_val):
            nonlocal res
            
            if not root:
                return 0
            print(root.val)
            if root.val >= max_val:
                max_val = root.val
                res += 1
            
            dfs(root.right, max_val)
            dfs(root.left, max_val)
        dfs(root, float("-inf"))
        return res