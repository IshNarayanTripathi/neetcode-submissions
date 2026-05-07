# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr1, curr2 = l1, l2
        c = 0
        dummy = ListNode()
        prev = dummy
        while curr1 or curr2 or c:
            val1 = curr1.val if curr1 else 0
            val2 = curr2.val if curr2 else 0
            total = val1+val2+c
            c = total//10
            curr_val = total%10
            dummy.next = ListNode(curr_val)
            dummy = dummy.next
            if curr1: curr1 = curr1.next
            if curr2: curr2 = curr2.next
        return prev.next