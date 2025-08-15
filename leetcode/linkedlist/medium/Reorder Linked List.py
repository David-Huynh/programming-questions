# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Find length of list
        # Flip the second half in place
        # combine the two lists

        # find length of list
        length = 0
        point = head
        while point:
            length += 1
            point=point.next
        # Move to start of second half
        second_half_head = head
        saved_node = None
        for i in range(length//2 + 1):
            if i == length//2:
                saved_node = second_half_head
            second_half_head = second_half_head.next
        saved_node.next = None
        # Flip the second half
        prev = None
        curr = second_half_head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        first_head = head
        second_half_head = prev
        while second_half_head:
            temp = first_head.next
            first_head.next = second_half_head
            temp2 = second_half_head.next
            second_half_head.next = temp
            first_head = temp
            second_half_head = temp2
