# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        prev = dummy
        curr1, curr2 = list1, list2
        while curr1 and curr2:
            if  curr1.val < curr2.val:
                new_node = ListNode(curr1.val)
                prev.next = new_node
                prev = new_node
                curr1 = curr1.next
            else:
                new_node = ListNode(curr2.val)
                prev.next = new_node
                prev = new_node
                curr2 = curr2.next
        while curr1:
            new_node = ListNode(curr1.val)
            prev.next = new_node
            prev = new_node
            curr1 = curr1.next
        while curr2:
            new_node = ListNode(curr2.val)
            prev.next = new_node
            prev = new_node
            curr2 = curr2.next
        return dummy.next


