# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast, slow = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        new_curr = slow.next
        slow.next = None
        prev = None
        while new_curr:
            _next = new_curr.next
            new_curr.next = prev
            prev = new_curr
            new_curr = _next
        curr = head
        while curr and prev:
            curr_next = curr.next
            prev_next = prev.next
            curr.next = prev
            prev.next = curr_next
            curr = curr_next
            prev = prev_next
        
