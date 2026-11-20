# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next
        median = math.ceil(length/2)
        i = 0
        dummy = prev = ListNode()
        curr = head
        while i != median:
            prev.next = curr
            prev = curr
            curr = curr.next
            i += 1
        second = prev.next
        prev.next = None
        sp = None
        cu = second
        while cu:
            nxt = cu.next
            cu.next = sp
            sp = cu
            cu = nxt
        alter = True
        curr = head
        while curr and sp:
            cn = curr.next
            sn = sp.next
            curr.next = sp
            sp.next = cn
            curr = cn
            sp = sn
        


        
        