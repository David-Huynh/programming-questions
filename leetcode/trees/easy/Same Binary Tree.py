# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # TWO q's pop same time if ever diff return false 
        # Else return true
        p_q = []
        q_q = []
        p_q.append(p)
        q_q.append(q)
        while p_q and q_q:
            node_p = p_q.pop(0)
            node_q = q_q.pop(0)
            if (node_p and not node_q) or (node_q and not node_p):
                return False
            if node_p and node_q:
                if not node_p.val == node_q.val:
                    return False
                p_q.append(node_p.left)
                p_q.append(node_p.right)
                q_q.append(node_q.left)
                q_q.append(node_q.right)

        return True