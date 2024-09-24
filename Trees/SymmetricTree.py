'''
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        
        return self.checkSymmetry(root.left, root.right)

    def checkSymmetry(self, leftRoot: TreeNode, rightRoot: TreeNode) -> bool:
        if leftRoot is None and rightRoot is None:
            return True

        if leftRoot is None or rightRoot is None:
            return False

        return leftRoot.val == rightRoot.val and self.checkSymmetry(leftRoot.left, rightRoot.right) and self.checkSymmetry(leftRoot.right, rightRoot.left)