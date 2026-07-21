# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        def search(node):
            if val > node.val:
                if node.right:
                    search(node.right)
                else:
                    node.right = TreeNode(val)
                    return
            else:
                if node.left:
                    search(node.left)
                else:
                    node.left = TreeNode(val)
                    return
        if root:
            search(root)
        else:
            root = TreeNode(val)
        return root
