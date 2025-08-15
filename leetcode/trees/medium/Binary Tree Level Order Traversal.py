# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # this is the other question with depth but when same depth then add to the same nested list
        q = []
        traversal_order = {}
        q.append((root,0))
        while q:
            node, index = q.pop(0)
            if node:
                traversal_order[index] = traversal_order.get(index, []) + [node.val]
                q.append((node.left,index+1))
                q.append((node.right,index+1))
        order = []
        for key in traversal_order:
            order.append(traversal_order[key])
        return order