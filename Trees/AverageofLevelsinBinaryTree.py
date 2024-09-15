'''
Given the root of a binary tree, return the average value of the nodes on each level in the form of an array. 
Answers within 10-5 of the actual answer will be accepted.
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return []

        q = [root]
        result = []

        while q:
            qlength = len(q)
            sum = 0

            for i in range(qlength):
                current = q.pop(0)
                sum += current.val

                if current.left:
                    q.append(current.left)
                if current.right:
                    q.append(current.right)

            result.append(sum / qlength)  

        return result