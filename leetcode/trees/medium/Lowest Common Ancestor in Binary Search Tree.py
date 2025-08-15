# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # the LCA is the last node that p and q share on the path to their nodes
        queue = []
        queue.append(root)

        while queue:
            node = queue.pop()
            if node:
                if (p.val >= node.val and q.val <= node.val) or (p.val<= node.val and q.val>=node.val): # If split then return this node
                    return node
                if p.val > node.val:
                    queue.append(node.right)
                else:
                    queue.append(node.left)
        return None

