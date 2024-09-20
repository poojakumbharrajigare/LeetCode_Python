'''
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = None

        if l1 is None and l2 is None:
            return None

        if l1 is None or l2 is None:
            head = l2 if l1 is None else l1
            return head

        if l1.val < l2.val:
            head = ListNode(l1.val)
            l1 = l1.next
        else:
            head = ListNode(l2.val)
            l2 = l2.next

        l = head
        while l1 is not None or l2 is not None:
            if l1 is None:
                head.next = l2
                return l

            if l2 is None:
                head.next = l1
                return l

            if l1.val < l2.val:
                head.next = ListNode(l1.val)
                head = head.next
                l1 = l1.next
            else:
                head.next = ListNode(l2.val)
                head = head.next
                l2 = l2.next

        return l