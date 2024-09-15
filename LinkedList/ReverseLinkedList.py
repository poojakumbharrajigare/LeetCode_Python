'''
Given the head of a singly linked list, reverse the list, and return the reversed list.
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        current = head
        previous = None

        while current:
            next = current.next
            current.next = previous
            previous = current
            current = next
        
        return previous