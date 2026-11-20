# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = i = 0
        curr = head
        while curr:
            length += 1
            curr =curr.next
        if length == n:
            if length == 1:
                return None
            else:
                return head.next
        target = length-n
        curr = head
        while i < target-1:
            i += 1
            curr = curr.next
        nxt = curr.next.next if curr.next else None
        curr.next = nxt
        return head

        