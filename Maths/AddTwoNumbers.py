'''
You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order, and each of their nodes contains a single digit. 
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        return self.newMethod(l1, l2, 0)

    def newMethod(self, next1: ListNode, next2: ListNode, carry: int) -> ListNode:
        if next1 is None and next2 is None and carry == 0:
            return None

        total = (next1.val if next1 is not None else 0) + (next2.val if next2 is not None else 0) + carry
        carry = total // 10
        val = total % 10

        return ListNode(val, self.newMethod(next1.next if next1 else None, next2.next if next2 else None, carry))