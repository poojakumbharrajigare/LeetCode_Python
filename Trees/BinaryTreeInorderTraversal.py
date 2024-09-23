'''
Given the root of a binary tree, return the inorder traversal of its nodes' values.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        self.inorderHelper(root, result)
        return result

    def inorderHelper(self, root: TreeNode, result: list[int]) -> None:
        if root is None:
            return

        self.inorderHelper(root.left, result)
        result.append(root.val)
        self.inorderHelper(root.right, result)