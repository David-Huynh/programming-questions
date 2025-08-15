# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # BFS with q and add depth to q :D or smth or pq idk brain fried no think 
        q = []
        q.append((root,1))
        max_depth = 0
        while q:
            node, depth = q.pop(0)
            if node:
                max_depth = max(max_depth, depth)
                q.append((node.left,depth+1))
                q.append((node.right,depth+1))
        return max_depth