# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # BFS but swap first before q
        q = []
        q.append(root)
        while q:
            node = q.pop(0)
            
            if node:
                temp = node.left
                node.left = node.right
                node.right = temp
                q.append(node.left)
                q.append(node.right)
        return root