'''
Given the root of a binary tree, return the postorder traversal of its nodes' values.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        self.postorder(root, result)

        return result

    def postorder(self, root: TreeNode, result: List[int]) -> None:
        if root is None:
            return
        
        self.postorder(root.left, result)
        self.postorder(root.right, result)
        result.append(root.val)