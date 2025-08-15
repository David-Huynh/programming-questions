# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        indicator_node = ListNode()
        node_pointer = head
        while node_pointer:
            if node_pointer == indicator_node:
                return True
            temp = node_pointer
            node_pointer = node_pointer.next
            temp.next = indicator_node 
            
        return False