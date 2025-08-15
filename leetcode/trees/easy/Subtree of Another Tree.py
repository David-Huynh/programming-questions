# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # save DFS traversal of subtree 
            #if any node in root matches start of subtree start dfs on root  
        # BFS on root till a node matches the start of the subroot
        sub_stack = []
        sub_traversal = []
        sub_stack.append(subRoot)
        while sub_stack:
            node = sub_stack.pop()
            if node:
                sub_stack.append(node.right)
                sub_stack.append(node.left)
                sub_traversal.append(node.val)
        
        q = []
        q.append(root)
        while q:
            node = q.pop(0)
            if node:
                if node.val == sub_traversal[0]:
                    index = 0
                    stack = []
                    stack.append(node)
                    while stack:
                        node_inside = stack.pop()
                         
                        if node_inside:
                            if index >= len(sub_traversal) or not node_inside.val == sub_traversal[index]:
                                break
                            stack.append(node_inside.right)
                            stack.append(node_inside.left)
                            index += 1

                    else:
                        if index < len(sub_traversal):
                            continue
                        else:
                            return True
                q.append(node.left)
                q.append(node.right)
        return False