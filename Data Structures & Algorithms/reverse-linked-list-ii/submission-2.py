# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        prior_list = None
        new_head = head
        if left != 1:
            count = left
            while count-1>0:
                prior_list = new_head
                new_head = new_head.next
                count -= 1
        jumps = right-left
        curr = new_head
        while jumps > 0:
            curr = curr.next
            jumps -= 1
        remaining = None
        if curr :
            remaining = curr.next
            curr.next = None
        prev = None
        dummyNode = first = new_head
        while first:
            _next = first.next
            first.next = prev
            prev = first
            first = _next
        #first.next = remaining
        dummyNode.next = remaining
        if not prior_list:
            return prev
        else:
            prior_list.next = prev
            return head




