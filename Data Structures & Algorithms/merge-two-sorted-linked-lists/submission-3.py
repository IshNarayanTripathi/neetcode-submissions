# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        prev = ListNode()
        dummy = prev
        l1, l2 = list1, list2
        while l1 and l2:
            if l1.val <= l2.val:
                dummy.next = l1
                dummy = l1
                l1 = l1.next
            else:
                dummy.next = l2
                dummy = l2
                l2 = l2.next
        while l1:
            dummy.next = l1
            dummy = l1
            l1 = l1.next
        while l2:
            dummy.next = l2
            dummy = l2
            l2 = l2.next 
        return prev.next
