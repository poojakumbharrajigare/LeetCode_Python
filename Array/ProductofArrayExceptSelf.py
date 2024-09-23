'''
Given an integer array nums, return an array answer such that 
answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.
'''

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result= [1] * n
        curr = 1

        for i in range(n):
            result[i] *= curr
            curr *= nums[i]

        curr = 1
        for i in range(n-1, -1, -1):
            result[i] *= curr
            curr *= nums[i]

        return result