'''
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left 
subtree
 of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        sortedList = []
        self.inorderTraverse(root, sortedList)

        for i in range(len(sortedList) - 1):
            if sortedList[i] >= sortedList[i+1]:
                return False

        return True

    def inorderTraverse(self, root: TreeNode, sortedList: List[int]):
        if root is not None:
            self.inorderTraverse(root.left, sortedList)
            sortedList.append(root.val)
            self.inorderTraverse(root.right, sortedList)

    