# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        new_list_head = ListNode()
        list_pointer = new_list_head
        if not list1 and not list2:
            return None
        while list1 or list2:
            if not list2 or (list1 and list1.val < list2.val):
                list_pointer.val = list1.val
                list1 = list1.next
            else:
                list_pointer.val = list2.val
                list2 = list2.next
            if list1 or list2:
                temp = ListNode()
                list_pointer.next = temp
                list_pointer = temp
        return new_list_head