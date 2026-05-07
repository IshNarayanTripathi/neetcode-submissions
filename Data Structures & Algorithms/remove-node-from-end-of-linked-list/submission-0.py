# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next
        pointer = length-n-1
        if pointer < 0:
            if head.next:
                return head.next
            return None
        curr = head
        while pointer > 0:
            curr = curr.next
            pointer -= 1
        if curr.next:
            curr.next = curr.next.next
        return head
        