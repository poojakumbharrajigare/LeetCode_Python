'''
Given the head of a singly linked list where elements are sorted in ascending order, convert it to a 
height-balanced binary search tree.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if head is None:
            return None
        
        return self.toBST(head, None)
    
    def toBST(self, head: ListNode, tail: ListNode) -> TreeNode:
        if head == tail:
            return None
        
        mid = self.findMid(head, tail)
        node = TreeNode(mid.val)
        node.left = self.toBST(head, mid)
        node.right = self.toBST(mid.next, tail)
        
        return node
    
    def findMid(self, head: ListNode, tail: ListNode) -> ListNode:
        slow = head
        fast = head
        
        while fast != tail and fast.next != tail:
            slow = slow.next
            fast = fast.next.next
        
        return slow